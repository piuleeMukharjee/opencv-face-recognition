# 🧠 Face Recognition with OpenCV


A beginner-friendly real-time **Face Recognition System** built using **OpenCV** and **Python**. This project leverages **Haar Cascade Classifier** for face detection and **LBPH Face Recognizer** for identifying known individuals. 🧑‍💻✨

---

## 🚀 Features

- 📷 Detects faces in grayscale using Haar Cascades
- 🏷️ Recognizes trained individuals with confidence scores
- 💾 Saves features and labels as `.npy` files
- 📊 Uses LBPH (Local Binary Patterns Histogram) algorithm
- 📂 Organized structure to train from image directories
- 🧪 Tested with real celebrity images like **MS Dhoni**, **Deepika Padukone**, etc.

---

## 🛠️ Tech Stack

| Tool           | Use                          |
|----------------|-------------------------------|
| Python         | Programming Language          |
| OpenCV         | Image processing & ML models  |
| NumPy          | Matrix operations             |
| VS Code        | Code Editor                   |

---

## 📦 Installation & Run

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/opencv-face-recognition.git
cd opencv-face-recognition

# Install dependencies
pip install opencv-python numpy

# Train the model
python faces_train.py

# Run recognition
python face_recognition.py
```
---

🧠 Understanding the Flow
Load images from img/ directory categorized by person name

Detect face using Haar cascade

Convert to grayscale and crop the ROI (Region of Interest)

Save face features and corresponding labels

Train using LBPH algorithm

Use trained model to recognize new faces in test images
---

🙌 Acknowledgements
Thanks to OpenCV and the Python community for such awesome tools to get started with computer vision! 🔍✨
---
## 📬 Connect with Me

<p align="center">
  <a href="https://www.linkedin.com/in/piulee-mukharjee-14a54b266/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn Button" />
  </a>
  <a href="piuleemukharjee@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail" alt="Email Button" />
  </a>
</p>


---
🔖 Hashtags
#OpenCV #Python #FaceRecognition #AI #ComputerVision #DeepLearning #LBPH #HaarCascade #WomenInTech #100DaysOfCode #ProjectShowcase

yaml
Copy
Edit


---

### ✅ Replace:
- `"YOUR_USERNAME"` with your GitHub username.
- Any email or LinkedIn links with your actual profile.
- Add real `.png` screenshots in a folder like `/screenshots` to match image paths.

Let me know if you want the `LICENSE`, a `.gitignore`, or a minimal version too!

