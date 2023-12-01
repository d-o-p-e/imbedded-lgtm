import os
from functools import lru_cache
import numpy as np
from numpy.typing import NDArray
import cv2
from cv2.typing import MatLike
import face_recognition

class Recognition:
    faces: dict[str, NDArray] = {}
    known_face_encodings: list[NDArray]
    known_face_names: list[str]

    def __init__(self):
        for filename in os.listdir('faces'):
            if filename == '.gitkeep':
                continue
            face_encoding = face_recognition.load_image_file(file=f'faces/{filename}')
            self.faces[filename.split('.')[0]] = face_recognition.face_encodings(face_encoding)[0]
        
        self.known_face_encodings = list(self.faces.values())
        self.known_face_names = list(self.faces.keys())
    
    def get_faces(self):
        return self.faces.keys()

    def update(self, name: str, ext: str):
        self.faces[name] = ext

        self.known_face_encodings = list(self.faces.values())
        self.known_face_names = list(self.faces.keys())

    def recognize(self, frame: MatLike):
        # frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            face_names.append(name)
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            # top *= 4
            # right *= 4
            # bottom *= 4
            # left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return frame    

recognition: Recognition

async def set_recognition():
    global recognition
    recognition = Recognition()

async def get_recognition():
    return recognition