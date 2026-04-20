# User Interface Elements for FNAF Game

class HUD:
    def __init__(self):
        self.power_display = PowerDisplay()
        self.camera_feed_display = CameraFeedDisplay()
        # Initialize other HUD elements here

    def update(self):
        # Update the HUD elements such as power and camera feed
        self.power_display.update()
        self.camera_feed_display.update()
        # More update logic here

class PowerDisplay:
    def __init__(self):
        self.power_level = 100  # Example power level initialization

    def update(self):
        # Logic to update power level display
        print(f"Power Level: {self.power_level}%")
        # Display power level on the HUD

class CameraFeedDisplay:
    def __init__(self):
        self.active_camera = None  # Placeholder for active camera

    def update(self):
        # Logic to update camera feed
        if self.active_camera:
            print(f"Camera Feed: {self.active_camera}")
        else:
            print("No camera feed active")
