import MicIcon from "@mui/icons-material/Mic";
import MicOffIcon from "@mui/icons-material/MicOff";
import VolumeUpIcon from "@mui/icons-material/VolumeUp";
import VolumeOffIcon from "@mui/icons-material/VolumeOff";
import { IconButton } from "@mui/material";
import { useContext } from "react";
import { WebRTCContext } from "../../context/webrtc";

const StreamPlayer = () => {
  const { isMicOn, setIsMicOn, isSoundOn, setIsSoundOn, remoteVideoRef } =
    useContext(WebRTCContext);
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <video
        id="remotevideo"
        style={{
          width: "48vw",
          height: "27vw",
          backgroundColor: "black",
          marginBottom: "2rem",
        }}
        ref={remoteVideoRef}
        autoPlay
      />
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "center",
          gap: "2rem",
          width: "48vw",
        }}
      >
        <IconButton
          onClick={() => {
            setIsSoundOn(!isSoundOn);
          }}
        >
          {isSoundOn ? (
            <VolumeUpIcon style={{ width: "2rem", height: "2rem" }} />
          ) : (
            <VolumeOffIcon
              style={{ width: "2rem", height: "2rem", color: "red" }}
            />
          )}
        </IconButton>
        <IconButton
          onClick={() => {
            setIsMicOn(!isMicOn);
          }}
        >
          {isMicOn ? (
            <MicIcon style={{ width: "2rem", height: "2rem" }} />
          ) : (
            <MicOffIcon
              style={{ width: "2rem", height: "2rem", color: "red" }}
            />
          )}
        </IconButton>
      </div>
    </div>
  );
};

export default StreamPlayer;
