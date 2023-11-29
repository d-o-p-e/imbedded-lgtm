import StreamPlayer from "../components/player/stream";

const StreamPage = () => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        width: "80vw",
        height: "100vh",
      }}
    >
      <h1>Stream</h1>
      <StreamPlayer />
      
    </div>
  );
};

export default StreamPage;
