import { RefObject } from "react";

export interface WebRTCContextType {
  isMicOn: boolean;
  setIsMicOn: (isMicOn: boolean) => void;
  isSoundOn: boolean;
  setIsSoundOn: (isSoundOn: boolean) => void;
  remoteVideoRef: RefObject<HTMLVideoElement>;
}
