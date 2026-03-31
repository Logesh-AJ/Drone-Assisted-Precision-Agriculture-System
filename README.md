# 🚁 Drone-Assisted Precision Agriculture System

AI-powered drone system for real-time sugarcane disease detection using YOLOv8 and Raspberry Pi edge computing.

---

## 🧠 Tech Stack

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy
* Raspberry Pi 4
* Quadcopter Drone (Pixhawk-based flight controller)
* High-resolution camera (USB / Insta360 / equivalent)

---

## 🚀 Key Features

* 🌿 Real-time sugarcane disease detection
* 🚁 Drone-based aerial monitoring
* ⚡ Edge AI processing using Raspberry Pi 4
* 📦 Onboard data storage (SD card)
* 🎯 Detection of multiple diseases:

  * Rust
  * Red Rot
  * Mosaic
  * Yellow Leaf Disease

---

## ⚙️ System Architecture

The system integrates UAV, edge computing, and AI:

* Drone captures aerial images
* Camera streams data to Raspberry Pi
* YOLOv8 model performs real-time detection
* Results stored and used for analysis

👉 According to the workflow diagram in the paper (*page 6*), the pipeline follows:
Image Capture → Preprocessing → YOLOv8 Inference → Output → Storage 

---

## ⚙️ Workflow

1. **Drone Deployment**

   * Quadcopter flies over sugarcane fields

2. **Image Acquisition**

   * High-resolution camera captures aerial images

3. **Data Transmission**

   * Frames sent to Raspberry Pi via USB

4. **Preprocessing**

   * Image resizing and normalization

5. **AI Inference**

   * YOLOv8 detects disease classes

6. **Output**

   * Bounding boxes + labels + confidence scores

7. **Storage**

   * Results saved locally for further analysis

---

## 🎥 Demo Videos

### 🌿 Sugarcane Disease Detection (Drone + YOLOv8)

Real-time disease detection in sugarcane crops using a drone-mounted camera and YOLOv8 deployed on Raspberry Pi edge hardware.

---

▶ [Video 1](https://youtube.com/shorts/ynZ7JyUP72Y?feature=share)

▶ [Video 2](https://youtube.com/shorts/ynZ7JyUP72Y)


---


## ⚡ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Logesh-AJ/Drone-Assisted-Precision-Agriculture-System.git
```

### 2. Navigate to project

```bash
cd Drone-Assisted-Precision-Agriculture-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run detection

```bash
python src/main.py
```

---

## ⚙️ System Requirements

* Python >= 3.8
* Raspberry Pi 4 (recommended for edge deployment)
* Camera (USB / drone-mounted camera)
* Drone system (Pixhawk or equivalent)
* OS: Linux / Windows

---

## 📦 Dependencies

* ultralytics
* opencv-python
* numpy

---

## 📁 Project Structure

```bash
Drone-Assisted-Precision-Agriculture-System/
 ├── src/
 ├── model/
 ├── output_images/
 ├── model_output_graphs/
 ├── demo_video
 ├── README.md
 └── requirements.txt
```

---

## 📄 Research Paper

This work is published in IEEE conference (ICVTTS 2025).

👉 View details:
`paper_link.md`

---

## 📊 Key Insights

* Edge AI reduces latency by avoiding cloud dependency
* Drone-based monitoring enables large-scale coverage
* Early disease detection improves crop yield and reduces loss

---

## 🚧 Challenges

* Limited real-time performance on Raspberry Pi
* Dataset variability (lighting, environment, crop stage)
* Hardware constraints (battery, payload)

---

## 🚀 Future Improvements

* Model optimization for higher FPS
* Integration with autonomous navigation
* Multispectral / thermal imaging
* Disease hotspot mapping

---

## 📌 Applications

* Precision agriculture
* Crop disease monitoring
* Smart farming systems
* Large-scale farm analytics

---

## 👤 Author

**Logesh A J**
AI | Computer Vision | Embedded Systems

---
