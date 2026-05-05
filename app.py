from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import base64

app = Flask(__name__)

# ── Load AI Models ─────────────────────────────────────────
age_net    = cv2.dnn.readNet("age_net.caffemodel",    "deploy_age.prototxt")
gender_net = cv2.dnn.readNet("gender_net.caffemodel", "deploy_gender.prototxt")

# OpenCV built-in face detector (no mediapipe needed)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

AGE_BUCKETS = ['(0-2)','(4-6)','(8-12)','(15-20)',
               '(25-32)','(38-43)','(48-53)','(60-100)']
GENDER_LIST = ['Male', 'Female']
MODEL_MEAN  = (78.4263377603, 87.7689143744, 114.895847746)

# ── Routes ─────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Decode base64 image from browser
        img_data  = data["image"].split(",")[1]
        img_bytes = base64.b64decode(img_data)
        np_arr    = np.frombuffer(img_bytes, np.uint8)
        frame     = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        h, w = frame.shape[:2]

        # Detect faces
        detected = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60)
        )

        faces = []

        for (x, y, fw, fh) in detected:
            x1 = max(0, x - 20)
            y1 = max(0, y - 20)
            x2 = min(w, x + fw + 20)
            y2 = min(h, y + fh + 20)

            face = frame[y1:y2, x1:x2]
            if face.size == 0:
                continue

            blob = cv2.dnn.blobFromImage(
                face, 1.0, (227, 227), MODEL_MEAN, swapRB=False
            )

            # Gender prediction
            gender_net.setInput(blob)
            gender_preds = gender_net.forward()
            gender       = GENDER_LIST[gender_preds[0].argmax()]
            gender_conf  = float(gender_preds[0].max()) * 100

            # Age prediction
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age       = AGE_BUCKETS[age_preds[0].argmax()]
            age_conf  = float(age_preds[0].max()) * 100

            faces.append({
                "gender":            gender,
                "gender_confidence": round(gender_conf, 1),
                "age":               age,
                "age_confidence":    round(age_conf, 1),
                "box":               [x1, y1, x2, y2]
            })

        return jsonify({"faces": faces, "count": len(faces)})

    except Exception as e:
        return jsonify({"error": str(e), "faces": [], "count": 0})


if __name__ == "__main__":
    app.run(debug=True)