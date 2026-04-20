import cv2
import numpy as np

class CameraFeed:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(camera_index)

    def get_frame(self):
        # Capture frame-by-frame
        ret, frame = self.capture.read()
        if not ret:
            raise ValueError("Could not read frame from the camera.")
        return frame

    def release(self):
        # Release the capture
        self.capture.release()

    def show_feed(self):
        while True:
            frame = self.get_frame()
            # Display the resulting frame
            cv2.imshow('Camera Feed', frame)
            
            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = CameraFeed(camera_index=0)
    camera.show_feed()