import cv2
from ultralytics import YOLO

# Define image path and load the YOLO model
img_pth = "test/images/img-107_jpg.rf.2e40485785f6e5e2efec404301b235c2.jpg"
model = YOLO("best.pt")

# Perform detection
results = model(source=img_pth)

# Load the image
image = cv2.imread(img_pth)

# Define a function to determine the color based on object size
def get_box_color(width, height):
    if width >= 150 and height >= 150:
        return (0, 0, 255)  # Red for large objects
    else:
        return (0, 255, 0)  # Green for small objects

# Extract results and annotate the image
for result in results[0].boxes.data:  # Iterate through each detection
    x1, y1, x2, y2, conf, cls = result[:6]  # Bounding box and other details
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    width = x2 - x1
    height = y2 - y1

    # Get the color based on width and height
    box_color = get_box_color(width, height)

    # Draw the bounding box
    cv2.rectangle(image, (x1, y1), (x2, y2), box_color, 2)

    # Annotate with width and height
    label = f"W:{width}, H:{height}"
    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 2)

# Display the result
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
