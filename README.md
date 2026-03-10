https://github.com/user-attachments/assets/d996e787-34c0-4a9c-9949-620392179f27

  
[README_pothole.md](https://github.com/user-attachments/files/25751168/README_pothole.md)
# 🚧 Pothole Detection & Classification System with YOLOv8

> Detect potholes in real-time, classify them by size, and send instructions to hardware to simulate car responses!

---

## Table of Contents

1. [About The Project](#about-the-project)
   - [Built With](#built-with)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)
4. [Roadmap](#roadmap)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)
8. [Acknowledgments](#acknowledgments)

---

## About The Project

A smart pothole detection system using **YOLOv8** that:

- 🎯 Detects potholes from video or camera input.
- 📏 Classifies potholes by size: **Small**, **Medium**, **Large**.
- 🔌 Sends size-based instructions to microcontrollers to simulate car behavior.
- 🖼️ Provides visual feedback with bounding boxes and labels.

Perfect for autonomous driving simulations, vehicle safety research, or embedded hardware prototyping.

**Features:**

- **Real-time detection** using YOLOv8
- **Size classification** based on bounding box area
- **Hardware integration**: Controls actuators like LEDs, servos, or motors to simulate car reactions
- **Visual feedback**: Bounding boxes with size labels
- **Extensible**: Easily add depth estimation or multiple pothole handling

**Dataset:**

This project uses the [Pothole Detection Dataset on Kaggle](https://www.kaggle.com/datasets/harsha547/potholes-in-roads), where images are annotated for pothole location and size. You can also use your own custom images with YOLO-compatible annotations.

> ⚠️ **Disclaimer**: This system is for **simulation/testing only**. Do not connect directly to real vehicles without proper safety measures. Make sure actuators are set up safely for testing.

[🔝 back to top](#table-of-contents)

---

## Built With

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?style=for-the-badge)
- ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
- ![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white)
- ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white)
- PySerial
- Arduino / Raspberry Pi / Jetson Nano

[🔝 back to top](#table-of-contents)

---

## Getting Started

Here's how to get the pothole detection system running locally.

### Prerequisites

Make sure you have **Python 3.x** installed, then install the required packages:

```bash
pip install ultralytics opencv-python pyserial
```

### Installation

1. Clone the repo

```bash
git clone https://github.com/your_username/pothole-detection.git
```

2. Navigate into the project directory

```bash
cd pothole-detection
```

3. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/harsha547/potholes-in-roads) and place it in the `/data` folder, or use your own YOLO-annotated images.

4. Connect your microcontroller (Arduino / Raspberry Pi / Jetson Nano) and configure the serial port in `pothole_detection.py`:

```python
SERIAL_PORT = 'COM3'  # Update to your port (e.g., '/dev/ttyUSB0' on Linux)
```

[🔝 back to top](#table-of-contents)

---

## Usage

Run the detection script:

```bash
python pothole_detection.py
```

The system will:

1. Open the video/camera feed.
2. Detect potholes in real-time using YOLOv8.
3. Classify each pothole by size based on bounding box area.
4. Send size-based serial commands to the connected microcontroller.
5. Display bounding boxes with size labels on the live feed.



For more examples, please refer to the [Documentation](#)

[🔝 back to top](#table-of-contents)

---

## Roadmap

- [x] Real-time pothole detection with YOLOv8
- [x] Size classification (Small / Medium / Large)
- [x] Serial communication with microcontroller
- [x] Bounding box visual feedback
- [x] Depth estimation integration
- [x] Multi-pothole simultaneous handling
- [x] GPS tagging for detected potholes 📍
- [x] Web dashboard for live monitoring


See the [open issues](https://github.com/your_username/pothole-detection/issues) for a full list of proposed features and known issues.

[🔝 back to top](#table-of-contents)

---

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also open an issue with the tag `enhancement`. Don't forget to ⭐ the project — thanks!


[🔝 back to top](#table-of-contents)


---

## Contact

Tarun Malepati
(further details in my profile)

Project Link: [[https://github.com/your_username/pothole-detection](https://github.com/your_username/pothole-detection)](https://github.com/TarunMalepati99/Pothole_detection)

[🔝 back to top](#table-of-contents)

---

## Acknowledgments

Resources and tools that made this project possible:

- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com)
- [Kaggle: Potholes in Roads Dataset](https://www.kaggle.com/datasets/harsha547/potholes-in-roads)
- [OpenCV Documentation](https://docs.opencv.org)
- [PySerial Docs](https://pyserial.readthedocs.io)
- [Choose an Open Source License](https://choosealicense.com)
- [Img Shields](https://shields.io)
- [GitHub Pages](https://pages.github.com)
- [Arduino Getting Started](https://www.arduino.cc/en/Guide)

[🔝 back to top](#table-of-contents)

---

> *Built for safer roads and smarter vehicles. 🚗💡*
