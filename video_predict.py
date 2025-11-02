import cv2
from ultralytics import YOLO
import torch

# Load the YOLOv8 model
model = YOLO("best.pt")

# Input video file path
video_path = "2.mp4"

# Open the video file
video_capture = cv2.VideoCapture(video_path)

# Get video frame dimensions
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))

# Define the codec and create a VideoWriter object to save the output video
output_path = "output_video.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, 30, (frame_width, frame_height))

# Function to determine the bounding box color based on size
def get_box_color(width, height):
    if width >= 150 and height >= 150:
        return (0, 0, 255)  # Red for large boxes
    else:
        return (0, 255, 0)  # Green for small boxes

with torch.no_grad():
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Perform object detection using YOLOv8 on the current frame
        results = model(frame)

        for result in results[0].boxes.data:
            x1, y1, x2, y2, conf, cls = result[:6]  # Extract bounding box data
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            width = x2 - x1
            height = y2 - y1

            # Determine bounding box color based on size
            box_color = get_box_color(width, height)

            # Draw the bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)

            # Display width and height as a label
            label = f"W:{width}, H:{height}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 2)

        # Display the frame with detected objects
        cv2.imshow("Video Prediction", frame)

        # Write the frame to the output video
        out.write(frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and output objects
video_capture.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
