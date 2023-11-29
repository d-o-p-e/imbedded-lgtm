import { Button } from "@mui/material";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div
      style={{
        width: "calc(20vw - 2rem)",
        height: "calc(100vh - 2rem)",
        padding: "1rem",
        backgroundColor: "#f5f5f5",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Link to="/">
        <h1
          style={{
            padding: "1rem",
          }}
        >
          LGTM
        </h1>
      </Link>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: "1rem",
        }}
      >
        <Link to="/">
          <Button>Stream</Button>
        </Link>
        <Link to="/video">
          <Button>Videos</Button>
        </Link>
        {/* <Link to="/settings">
          <Button>Settings</Button>
        </Link> */}
      </div>
    </div>
  );
};

export default Navbar;
