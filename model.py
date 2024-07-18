import cv2
import pygame
import threading
from ultralytics import YOLO

# Load the YOLOv8 model (replace with your trained model path)
model = YOLO("yolov8n.pt")

# Initialize video capture (replace with your video source)
cap = cv2.VideoCapture("Security_Footabe_Live.mp4")

# Set parameters for violence detection
violence_classes = ["fighting", "shooting", "stabbing"]  

# Initialize Pygame for audio alerts
pygame.mixer.init()

# Load the alert sound (replace with your own sound file)
alert_sound = pygame.mixer.Sound("alarm.mp3")

def play_alert_sound():
    alert_sound.play()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection on the current frame
    results = model(frame)

    for result in results.pred[0]:
        label, confidence, bbox = result.tolist()
        x, y, w, h = map(int, bbox)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draw red bounding box
        cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Check if the detected label corresponds to violence
        if label in violence_classes:
            print("Violence detected!")
            # Play the alert sound in a separate thread
            alert_thread = threading.Thread(target=play_alert_sound)
            alert_thread.start()

    # Display the frame
    cv2.imshow("YOLOv8 Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()