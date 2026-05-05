# 🎭 FaceIQ — Real-Time AI Face Age & Gender Detection

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00C896?style=for-the-badge)

A real-time web app that uses your webcam to detect faces and predict **age range** and **gender** using deep learning — live in the browser, no installation needed on the client side.

---

## 🚀 Features

- 🎥 Live webcam feed with real-time face detection
- 👨👩 Gender prediction (Male / Female) with confidence %
- 🎂 Age range estimation across 8 buckets (e.g. 25–32)
- 👥 Multi-face support — detects multiple faces at once
- 📊 Live confidence bars per face
- 🌙 Dark sci-fi UI with glowing bounding boxes

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| ML / CV | OpenCV DNN, Caffe Models, Haar Cascade |
| Frontend | HTML5, CSS3, Vanilla JavaScript, WebRTC |

---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/YourUsername/face-analyzer.git
cd face-analyzer

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

### Download Model Files

Download these 4 files from [here](https://github.com/smahesh29/Gender-and-Age-Detection) and place them in the root folder:

- `deploy_age.prototxt`
- `age_net.caffemodel` (~50 MB)
- `deploy_gender.prototxt`
- `gender_net.caffemodel` (~50 MB)

---

## ▶️ Run

```bash
python app.py
```

Open Chrome → `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
face-analyzer/
├── templates/
│   └── index.html          # Frontend UI
├── static/
├── app.py                  # Flask backend + ML API
├── deploy_age.prototxt
├── age_net.caffemodel
├── deploy_gender.prototxt
├── gender_net.caffemodel
└── requirements.txt
```

---

## 📡 API

**POST** `/predict`

```json
// Request
{ "image": "data:image/jpeg;base64,..." }

// Response
{
  "count": 1,
  "faces": [{
    "gender": "Male",
    "gender_confidence": 96.3,
    "age": "(25-32)",
    "age_confidence": 74.1,
    "box": [120, 80, 280, 300]
  }]
}
```

---

## 🙏 Credits

- Age & Gender Caffe models by [Gil Levi & Tal Hassner](https://talhassner.github.io/home/projects/Adience/Adience-data.html)
- [OpenCV](https://opencv.org) · [Flask](https://flask.palletsprojects.com)

---

<div align="center">
Made with ❤️ by Ak &nbsp;|&nbsp; ⭐ Star this repo if it helped you!
</div>
