import { createBrowserRouter } from "react-router-dom";
import StreamPage from "./page/stream";
import VideoPage from "./page/video";
import Page from "./page/layout";
import SettingsPage from "./page/settings";

export const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <Page>
        <StreamPage />
      </Page>
    ),
  },
  {
    path: "/video",
    element: (
      <Page>
        <VideoPage />
      </Page>
    ),
  },
  {
    path: "/settings",
    element: (
      <Page>
        <SettingsPage />
      </Page>
    ),
  },
]);
