# 🎭 FaceIQ — Real-Time AI Face Age & Gender Detection

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-00C896?style=for-the-badge)

<br/>

> **FaceIQ** is a real-time AI web application that uses your webcam to detect faces and predict age range and gender — live in your browser, powered by deep learning.

<br/>

[🚀 Features](#-features) &nbsp;·&nbsp; [📁 Project Structure](#-project-structure) &nbsp;·&nbsp; [⚙️ Installation](#️-installation) &nbsp;·&nbsp; [🔍 How It Works](#-how-it-works) &nbsp;·&nbsp; [📡 API](#-api-reference) &nbsp;·&nbsp; [🌐 Deployment](#-deployment)

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#️-installation)
- [How to Use](#-how-to-use)
- [How It Works](#-how-it-works)
- [Model Files Explained](#-model-files-explained)
- [API Reference](#-api-reference)
- [Deployment](#-deployment)
- [Common Errors & Fixes](#-common-errors--fixes)
- [Future Improvements](#-future-improvements)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 🧠 About the Project

**FaceIQ** is a machine learning web application built from scratch using **Python**, **Flask**, and **OpenCV**. It opens your webcam inside the browser, captures frames, sends them to a Flask REST API, runs them through pre-trained deep learning models, and returns real-time predictions for:

- 👤 **Gender** — Male or Female with a confidence percentage
- 🎂 **Age Range** — One of 8 age buckets (e.g. 25–32) with a confidence percentage

The app uses **Caffe deep learning models** (trained on the Adience dataset with 26,000+ real face images) for predictions and **OpenCV Haar Cascade** for fast face detection — no heavy frameworks like TensorFlow or PyTorch needed.

The frontend is a **dark sci-fi themed UI** with glowing bounding boxes, live confidence bars, FPS counter, latency display, and per-face result cards — all updating in real time.

This project covers:
- Computer Vision (face detection)
- Deep Learning inference (OpenCV DNN module)
- REST API design (Flask)
- Frontend integration (WebRTC webcam + Fetch API)
- Web deployment

---

## ✨ Features

- 🎥 **Live webcam feed** — opens directly in the browser using WebRTC
- 🤖 **Real-time AI predictions** — age and gender estimated every 800ms
- 👨👩 **Gender detection** — Male or Female with confidence score
- 🎂 **Age range estimation** — predicts from 8 age buckets
- 📊 **Live confidence bars** — visual bars for each prediction score
- 🔲 **Glowing face bounding boxes** — color-coded by gender (cyan = male, pink = female)
- 👥 **Multi-face support** — detects and analyzes multiple faces simultaneously
- ⚡ **FPS & latency display** — live performance metrics shown on screen
- 🃏 **Per-face result cards** — each detected face gets its own result card on the right panel
- 🌙 **Dark sci-fi UI** — animated scan line, grid background, corner accents on bounding boxes
- 📱 **Responsive design** — works on both desktop and mobile browsers
- 🌐 **100% browser-based** — no app install needed on the client side
- 🔌 **Clean REST API** — `/predict` endpoint usable from any client

---

## 🛠️ Tech Stack

### Backend

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Core programming language |
| **Flask** | Web framework & REST API server |
| **OpenCV (cv2)** | Image processing & DNN inference |
| **NumPy** | Array operations for image data |
| **Base64** | Image encoding/decoding between browser and server |

### Machine Learning

| Technology | Purpose |
|-----------|---------|
| **OpenCV DNN Module** | Runs pre-trained Caffe deep learning models |
| **Caffe Age Model** | Predicts age range from a cropped face image |
| **Caffe Gender Model** | Predicts gender from a cropped face image |
| **Haar Cascade Classifier** | Fast face detection built into OpenCV |
| **Adience Dataset** | Dataset the Caffe models were originally trained on |

### Frontend

| Technology | Purpose |
|-----------|---------|
| **HTML5** | Page structure |
| **CSS3** | Styling, animations, responsive grid layout |
| **Vanilla JavaScript** | Webcam capture, API calls, canvas drawing |
| **WebRTC (getUserMedia)** | Access browser webcam |
| **Canvas API** | Draw bounding boxes and labels over the video |
| **Fetch API** | Send frames to Flask backend asynchronously |
| **Google Fonts** | Bebas Neue, DM Sans, JetBrains Mono |

---

## 📁 Project Structure

```
face-analyzer/
│
├── templates/
│   └── index.html              # Complete frontend — single file UI
│                               #   • Webcam feed with canvas overlay
│                               #   • Live face result cards (right panel)
│                               #   • FPS / latency / face count bar
│                               #   • Start / Stop camera controls
│                               #   • Dark sci-fi theme with animations
│
├── static/
│   ├── css/                    # Reserved for future separated CSS files
│   └── js/                     # Reserved for future separated JS files
│
├── app.py                      # Flask application entry point
│                               #   • Loads AI models on startup
│                               #   • GET  /         → serves index.html
│                               #   • POST /predict  → runs ML inference
│                               #   • Returns JSON with face predictions
│
├── deploy_age.prototxt         # Age neural network architecture (plain text)
├── age_net.caffemodel          # Age neural network weights (~50 MB binary)
├── deploy_gender.prototxt      # Gender neural network architecture (plain text)
├── gender_net.caffemodel       # Gender neural network weights (~50 MB binary)
│
├── requirements.txt            # All Python dependencies with versions
├── .gitignore                  # Git ignored files (venv, __pycache__, etc.)
└── README.md                   # This file
```

---

## ⚙️ Installation

### Prerequisites

Make sure you have these installed before starting:

- ✅ Python 3.8 or higher → [Download Python](https://www.python.org/downloads/)
- ✅ pip (comes with Python)
- ✅ Git → [Download Git](https://git-scm.com/)
- ✅ A working webcam
- ✅ Google Chrome browser (recommended)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YourUsername/face-analyzer.git
cd face-analyzer
```

---

### Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

You will see `(venv)` appear at the start of your terminal. ✅

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install flask opencv-python numpy
```

---

### Step 4 — Download AI Model Files

The 4 model files are **not included** in the repository because `.caffemodel` files are ~50MB each and exceed GitHub's recommended file size.

**Download from here:**

```
https://github.com/smahesh29/Gender-and-Age-Detection
```

Click **Code → Download ZIP**, extract it, and copy these 4 files into your `face-analyzer` root folder:

| File | Size | Description |
|------|------|-------------|
| `deploy_age.prototxt` | ~3 KB | Age model architecture definition |
| `age_net.caffemodel` | ~50 MB | Age model trained weights |
| `deploy_gender.prototxt` | ~3 KB | Gender model architecture definition |
| `gender_net.caffemodel` | ~50 MB | Gender model trained weights |

After placing them, your folder should look like:

```
face-analyzer/
├── templates/
├── static/
├── app.py
├── deploy_age.prototxt       ✅
├── age_net.caffemodel        ✅
├── deploy_gender.prototxt    ✅
└── gender_net.caffemodel     ✅
```

---

### Step 5 — Run the Application

```bash
python app.py
```

You should see this in your terminal:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

---

### Step 6 — Open in Browser

Open **Google Chrome** and go to:

```
http://127.0.0.1:5000
```

---

## 🎮 How to Use

1. Open `http://127.0.0.1:5000` in Chrome
2. Click the **▶ Start Camera** button
3. Allow camera permission when the browser asks
4. Look at your webcam — you will see:
   - A **glowing colored box** drawn around each face
   - **Gender and age range label** displayed on the box
   - **Result card** on the right panel with confidence bars
   - **Face count, FPS, and latency** displayed at the bottom
5. Multiple people can be detected at once — each gets their own card
6. Click **■ Stop** to turn off the camera

---

## 🔍 How It Works

### Full Pipeline

```
┌──────────────────────────────────────────────────────────┐
│                        BROWSER                           │
│                                                          │
│  Webcam (WebRTC getUserMedia)                            │
│      ↓                                                   │
│  Canvas captures frame every 800ms                       │
│      ↓                                                   │
│  Convert to Base64 JPEG (quality 0.75)                   │
│      ↓                                                   │
│  Fetch POST → /predict  { image: "data:image/jpeg..." }  │
└──────────────────────────────┬───────────────────────────┘
                               │ HTTP POST
                               ▼
┌──────────────────────────────────────────────────────────┐
│                      FLASK BACKEND                       │
│                                                          │
│  1. Receive JSON → decode Base64 → NumPy array           │
│  2. cv2.imdecode() → OpenCV BGR image                    │
│  3. Convert to Grayscale                                 │
│  4. Haar Cascade → find all face bounding boxes          │
│  5. For EACH detected face:                              │
│       a. Crop face + 20px padding                        │
│       b. blobFromImage() → 227×227, normalize colors     │
│       c. gender_net.forward() → [male%, female%]         │
│       d. age_net.forward()    → [p1, p2...p8 age ranges] │
│       e. argmax() → pick highest probability class       │
│       f. Multiply by 100 → confidence percentage         │
│  6. Build JSON response with all face results            │
└──────────────────────────────┬───────────────────────────┘
                               │ JSON Response
                               ▼
┌──────────────────────────────────────────────────────────┐
│                        BROWSER                           │
│                                                          │
│  1. Draw glowing boxes on canvas overlay                 │
│  2. Write gender + age label above each box              │
│  3. Draw corner accent marks on each box                 │
│  4. Update right panel with face result cards            │
│  5. Update face count, FPS, latency numbers              │
└──────────────────────────────────────────────────────────┘
```

### Key Functions Explained

| Function | File | What it does |
|----------|------|-------------|
| `face_cascade.detectMultiScale()` | app.py | Scans the image for all faces using Haar Cascade |
| `cv2.dnn.blobFromImage()` | app.py | Resizes face to 227×227 and normalizes pixel values |
| `gender_net.forward()` | app.py | Runs the gender DNN, returns 2 class probabilities |
| `age_net.forward()` | app.py | Runs the age DNN, returns 8 class probabilities |
| `argmax()` | app.py | Selects the class index with the highest probability |
| `getUserMedia()` | index.html | Requests webcam access from the browser |
| `sendFrame()` | index.html | Captures a video frame and sends it to Flask |
| `drawBoxes()` | index.html | Draws glowing colored boxes and labels on canvas |
| `updateCards()` | index.html | Renders face result cards in the right panel |

### Age Buckets — Why Ranges, Not Exact Age?

The age model predicts one of 8 age ranges rather than an exact number. This is because predicting an exact age from a face image is extremely difficult — faces at ages 30 and 35 look almost identical. Age ranges are much more reliable and accurate:

| Bucket | Age Range | Life Stage |
|--------|-----------|------------|
| 1 | 0 – 2 | Baby / Toddler |
| 2 | 4 – 6 | Young child |
| 3 | 8 – 12 | Older child |
| 4 | 15 – 20 | Teenager |
| 5 | 25 – 32 | Young adult |
| 6 | 38 – 43 | Middle aged |
| 7 | 48 – 53 | Older adult |
| 8 | 60 – 100 | Senior |

---

## 📦 Model Files Explained

### `.prototxt` files — The Blueprint

These are **plain text files** that define the neural network architecture — the number of layers, type of each layer (Convolution, ReLU, Pooling, Softmax, etc.), and how layers connect to each other. Think of it as the recipe or blueprint for building the neural network.

Example layer structure inside `deploy_age.prototxt`:

```
Input Layer      →  227×227 face image
Conv Layer 1     →  96 filters of size 7×7, stride 4
ReLU             →  Activation function (non-linearity)
Max Pooling      →  Reduces spatial size
Conv Layer 2     →  256 filters of size 5×5
ReLU + Pooling
...more layers...
Fully Connected  →  Flattens to 1D
Softmax Output   →  8 probabilities (one per age bucket)
```

### `.caffemodel` files — The Brain

These are **binary files** (cannot be opened in a text editor) containing millions of numerical values — the weights and biases — that the neural network learned during training on the **Adience dataset** (26,000+ real face images with age and gender labels collected in the wild).

These numbers encode what the network learned:
- Layer 1 learns basic edges and corners
- Layer 2 learns eyes, nose shapes
- Layer 3 learns full face features
- Final layers learn age and gender patterns

> **Analogy:** The `.prototxt` is the blank exam paper with all the questions. The `.caffemodel` is the answer sheet filled in after years of studying 26,000 faces.

### Why 4 Separate Files?

Age and gender are two **completely different classification problems** that require separate training:

- **Gender model** — 2-class problem → outputs `[Male probability, Female probability]`
- **Age model** — 8-class problem → outputs `[prob_0-2, prob_4-6, ..., prob_60-100]`

Each problem needs its own architecture (`.prototxt`) and its own trained weights (`.caffemodel`).

---

## 📡 API Reference

### `GET /`

Returns the main HTML page with the full webcam UI.

**Response:** `text/html` — the complete `index.html` page

---

### `POST /predict`

Accepts a Base64-encoded JPEG image captured from the browser webcam and returns all detected faces with age and gender predictions.

**Request:**

```http
POST /predict
Content-Type: application/json
```

```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgAB..."
}
```

**Success Response:**

```json
{
  "count": 2,
  "faces": [
    {
      "gender": "Male",
      "gender_confidence": 96.3,
      "age": "(25-32)",
      "age_confidence": 74.1,
      "box": [120, 80, 280, 300]
    },
    {
      "gender": "Female",
      "gender_confidence": 88.7,
      "age": "(15-20)",
      "age_confidence": 65.2,
      "box": [350, 90, 510, 310]
    }
  ]
}
```

**Error Response:**

```json
{
  "error": "Description of what went wrong",
  "faces": [],
  "count": 0
}
```

**Response Field Reference:**

| Field | Type | Description |
|-------|------|-------------|
| `count` | integer | Total number of faces detected in the frame |
| `faces` | array | List of face result objects |
| `gender` | string | `"Male"` or `"Female"` |
| `gender_confidence` | float | Prediction confidence 0–100 (%) |
| `age` | string | Age range string e.g. `"(25-32)"` |
| `age_confidence` | float | Prediction confidence 0–100 (%) |
| `box` | int[4] | Bounding box coordinates `[x1, y1, x2, y2]` in pixels |

---

## 🌐 Deployment

### Option 1 — Deploy on Render (Recommended Free Option)

**1. Install gunicorn:**
```bash
pip install gunicorn
pip freeze > requirements.txt
```

**2. Create `render.yaml` in your root folder:**
```yaml
services:
  - type: web
    name: faceiq
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

**3. Push everything to GitHub:**
```bash
git add .
git commit -m "Ready for Render deployment"
git push
```

**4. Deploy on Render:**
- Go to [render.com](https://render.com) and sign up
- Click **New → Web Service**
- Connect your GitHub repository
- Render automatically detects Python and deploys
- You receive a free public URL like `https://faceiq.onrender.com` ✅

> ⚠️ **Model Files Warning:** `.caffemodel` files are ~50MB each. GitHub recommends files under 50MB. If your push fails, add them to `.gitignore` and host the model files on Google Drive. Then write a script to download them at startup on the server.

---

### Option 2 — Deploy on Railway

**1. Create a `Procfile` in your root folder:**
```
web: gunicorn app:app
```

**2. Install gunicorn and update requirements:**
```bash
pip install gunicorn
pip freeze > requirements.txt
```

**3. Push to GitHub and go to [railway.app](https://railway.app)**
- New Project → Deploy from GitHub Repo
- Railway auto-detects Python and deploys automatically ✅

---

### Option 3 — Share on Local Network

To let others on the same WiFi access your app without deploying:

Change the last line of `app.py`:
```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

Run `python app.py` and find your local IP:
```bash
# Windows
ipconfig

# Mac / Linux
ifconfig
```

Share this URL with anyone on the same network:
```
http://YOUR_LOCAL_IP:5000
```

---

## 🐛 Common Errors & Fixes

| Error Message | Cause | Fix |
|---------------|-------|-----|
| `ModuleNotFoundError: flask` | Flask not installed | `pip install flask` |
| `ModuleNotFoundError: cv2` | OpenCV not installed | `pip install opencv-python` |
| `Error loading model` | Model files missing or wrong path | Place all 4 files in root folder same level as `app.py` |
| `AttributeError: module 'mediapipe' has no attribute 'solutions'` | Mediapipe version incompatibility | Remove mediapipe — the app now uses OpenCV face detection only |
| `Camera not working in browser` | Browser permissions blocked | Use Chrome → click camera icon in address bar → Allow |
| `OSError: [Errno 98] Address already in use` | Port 5000 is already being used | Change to `app.run(port=5001)` in `app.py` |
| `git push` fails — file too large | `.caffemodel` files > 100MB GitHub limit | Add to `.gitignore` and host model files separately |
| No faces detected | Bad lighting or face too small | Improve lighting and move closer to camera |

---

## 🚀 Future Improvements

- [ ] **Emotion detection** — happy, sad, angry, surprised, neutral
- [ ] **Face landmark detection** — 68 facial keypoints
- [ ] **Snapshot capture button** — save the current frame as an image
- [ ] **Results export** — download all predictions as a CSV file
- [ ] **Face count history chart** — graph of detections over time
- [ ] **Multiple camera support** — switch between available cameras
- [ ] **Mobile PWA** — installable as a Progressive Web App
- [ ] **Docker support** — fully containerized one-command deployment
- [ ] **GPU acceleration** — faster inference with CUDA support
- [ ] **Model download script** — auto-download models at first startup

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, copy, modify, merge, publish, distribute, and sell this software.

```
MIT License — Copyright (c) 2025 Ak
```

See the full license text at [opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)

---

## 🙏 Acknowledgements

- **Gil Levi & Tal Hassner** — Original Age and Gender Caffe models trained on the Adience dataset
  - Paper: *Age and Gender Classification using Convolutional Neural Networks* (IEEE CVPR Workshop, 2015)
  - [Project Page](https://talhassner.github.io/home/projects/Adience/Adience-data.html)
- **OpenCV Team** — Open Source Computer Vision Library → [opencv.org](https://opencv.org)
- **Flask Team** — Lightweight Python web framework → [flask.palletsprojects.com](https://flask.palletsprojects.com)
- **smahesh29** — Compiled and hosted the model files on GitHub → [GitHub Repo](https://github.com/smahesh29/Gender-and-Age-Detection)

---

<div align="center">

**Built with ❤️ by Ak**

Student · Government Polytechnic Palanpur · Cyber Security & Digital Forensics

<br/>

⭐ **If this project helped you, please star the repo!** ⭐

</div>
