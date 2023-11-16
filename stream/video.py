import cv2
from functools import lru_cache

from enums.quality import Quality

class Video():

    cap: cv2.VideoCapture
    width: int
    height: int

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.width = int(self.cap.get(3))
        self.height = int(self.cap.get(4))
        print(f'Video: {self.width}x{self.height}')
    
    def get_frames(self, quality: Quality = Quality.HIGH):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            if quality != Quality.HIGH:
                frame = cv2.resize(frame, (int(self.width / (int(quality.value) + 1)), int(self.height / (int(quality.value) + 1))))
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
            bytearray(buffer.tobytes()) + b'\r\n')

    def __del__(self):
        print('Video: Release')
        self.cap.release()

@lru_cache()
def get_video():
    return Video()