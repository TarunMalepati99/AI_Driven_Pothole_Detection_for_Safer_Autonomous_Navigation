import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("best.pt")

# Function to determine bounding box color based on size
def get_box_color(width, height):
    if width >= 150 and height >= 150:
        return (0, 0, 255)  # Red for large objects
    else:
        return (0, 255, 0)  # Green for small objects

# Function to upload image
def upload_image():
    global img_path, img_label
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if img_path:
        # Display uploaded image in the GUI
        img = Image.open(img_path)
        img.thumbnail((400, 400))  # Resize for display
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

# Function to predict and display results
def predict():
    global img_path
    if not img_path:
        result_label.config(text="Please upload an image first!", fg="red")
        return

    # Perform prediction
    results = model(source=img_path)
    image = cv2.imread(img_path)

    # Annotate the image with bounding boxes and dimensions
    pothole_info = []
    for result in results[0].boxes.data:
        x1, y1, x2, y2, _, _ = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        width = x2 - x1
        height = y2 - y1

        # Determine bounding box color
        box_color = get_box_color(width, height)

        # Draw bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), box_color, 2)

        # Annotate with width and height
        label = f"W:{width}, H:{height}"
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 2)

        # Store pothole info for display
        pothole_info.append(f"Pothole: W={width}, H={height}")

    # Convert result to Tkinter-compatible format
    result_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result_img = Image.fromarray(result_img)
    result_img.thumbnail((400, 400))  # Resize for display
    result_img = ImageTk.PhotoImage(result_img)

    # Update GUI with the annotated image
    img_label.config(image=result_img)
    img_label.image = result_img

    # Display results in text form
    result_label.config(text="\n".join(pothole_info), fg="blue")

# Create GUI window
window = tk.Tk()
window.title("Self-Driving Car Sensors")
window.geometry("600x700")
window.configure(bg="#f0f8ff")

# Heading
header = Label(window, text="Pothole Detection", font=("Arial", 20, "bold"), bg="#4682b4", fg="white")
header.pack(pady=10, fill="x")

# Image display area
img_label = Label(window, bg="#f0f8ff", relief="groove")
img_label.pack(pady=10, padx=10, ipadx=10, ipady=10)

# Buttons for Upload and Predict
button_frame = tk.Frame(window, bg="#f0f8ff")
button_frame.pack(pady=20)

upload_btn = Button(button_frame, text="Upload Image", font=("Arial", 12), bg="#4caf50", fg="white", command=upload_image)
upload_btn.grid(row=0, column=0, padx=10)

predict_btn = Button(button_frame, text="Predict", font=("Arial", 12), bg="#ff5722", fg="white", command=predict)
predict_btn.grid(row=0, column=1, padx=10)

# Label for displaying results
result_label = Label(window, text="", font=("Arial", 12), bg="#f0f8ff", fg="black", justify="left")
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()










