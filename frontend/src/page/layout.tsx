import Navbar from "../components/navbar/navbar";
import { WebRTCContextProvider } from "../context/webrtc";

const Page = ({ children }: { children: JSX.Element }) => {
  return (
    <WebRTCContextProvider>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
        }}
      >
        <Navbar />
        {children}
      </div>
    </WebRTCContextProvider>
  );
};

export default Page;
