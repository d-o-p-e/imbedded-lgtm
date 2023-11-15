from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse

from video import Video
from enums.quality import Quality

router = APIRouter(tags=["Stream"])

@router.get("/", description='Quality can be specified as a query parameter. 0 = HIGH, 1 = MEDIUM, 2 = LOW, default = HIGH')
def stream_live(video: Video = Depends(), quality: Quality = Quality.HIGH):
    return StreamingResponse(video.get_frames(quality=quality), media_type="multipart/x-mixed-replace; boundary=frame")