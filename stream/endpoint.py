from fastapi import APIRouter, Depends, UploadFile, Response
from fastapi.responses import StreamingResponse

from video import Video, get_video
from recognition import Recognition, get_recognition
from enums.quality import Quality

router = APIRouter(tags=["Stream"])

@router.get("/", description='Quality can be specified as a query parameter. 0 = HIGH, 1 = MEDIUM, 2 = LOW, default = HIGH\n Face recognition can be enabled by setting recognize_face to true')
def stream_live(video: Video = Depends(get_video), recognition: Recognition = Depends(get_recognition), quality: Quality = Quality.HIGH, recognize_face: bool = False):
    return StreamingResponse(video.get_frames(quality=quality, recognition=recognition, recognize_face=recognize_face), media_type="multipart/x-mixed-replace; boundary=frame")

@router.post("/register/{name}", description="Register a new face")
async def register_face(name: str, image: UploadFile):
    print(image.filename.split('.')[-1])
    with open(f"faces/{name}.{image.filename.split('.')[-1]}", "wb") as buffer:
        buffer.write(image.file.read())
    return Response(status_code=200)

@router.get("/faces", description="Get face list")
async def get_faces(recognition: Recognition = Depends(get_recognition)):
    return recognition.get_faces()