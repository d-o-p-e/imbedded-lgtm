import cv2
import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer
from socketio import AsyncClient

room_name = 'test'
socket = AsyncClient()
pc: RTCPeerConnection

async def getMedia():
    try:
        stream = MediaPlayer('/dev/video0', format='v4l2', options={
            'video_size': '640x480'
        })

        stream.video.stop()

        # stream.getTracks().forEach((track) => {
        #     if (!pcRef.current) {
        #       return;
        #     }
        #     pcRef.current.addTrack(track, stream);
        #   });

        # pc.addTrack(stream.audio)

        # pcRef.current.onicecandidate = (e) => {
        #     if (e.candidate) {
        #       if (!socketRef.current) {
        #         return;
        #       }
        #       console.log("recv candidate");
        #       socketRef.current.emit("candidate", e.candidate, roomName);
        #     }
        #   };

        @pc.on("track")
        async def on_track(track):
            print("recv track")
            if track.kind == "video":
                print("recv video track")
                cv2.imshow('frame', track)    
    except Exception as e:
        print(e)        
    
async def createOffer():
    try:
        print("create offer")
        sdp = await pc.createOffer()
        await pc.setLocalDescription(sdp)
        print("sent the offer")
        await socket.emit("offer", sdp, roomName=room_name)
    except Exception as e:
        print(e)

async def createAnswer(sdp: RTCSessionDescription):
    try:
        print("create answer")
        await pc.setRemoteDescription(sdp)
        answer = await pc.createAnswer()
        await pc.setLocalDescription(answer)
        print("sent the answer")
        await socket.emit("answer", answer, roomName=room_name)
    except Exception as e:
        print(e)


async def main():
    await socket.connect("https://signal.yanychoi.com")
    global pc
    pc = RTCPeerConnection(configuration={
        "iceServers": [
            {
                "urls": [
                    "stun:stun.l.google.com:19302",
                    "stun:stun1.l.google.com:19302",
                    "stun:stun2.l.google.com:19302",
                    "stun:stun3.l.google.com:19302",
                    "stun:stun4.l.google.com:19302",
                ]
            }
        ]
    })

    @pc.on("icecandidate")
    async def on_icecandidate(candidate):
        await socket.emit("candidate", candidate, roomName=room_name)

    @socket.on("all_users")
    async def on_all_users(users):
        createOffer()
    
    @socket.on("getOffer")
    async def on_getOffer(sdp: RTCSessionDescription):
        print("recv Offer")
        createAnswer(sdp)

    @socket.on("getAnswer")
    async def on_getAnswer(sdp: RTCSessionDescription):
        print("recv Answer")

        print("set remote description")
        await pc.setRemoteDescription(sdp)
    
    @socket.on("getCandidate")
    async def on_getCandidate(candidate):
        print("candidate")
        await pc.addIceCandidate(candidate)
    
    await socket.emit("join_room", data={"roomName": room_name})

    await getMedia()

    if socket.connected:
        await socket.disconnect()
    if pc:
        await pc.close()


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())