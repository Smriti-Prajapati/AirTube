# AirTube 🎯🖐️

Control YouTube using **hand gestures** — no mouse, no keyboard.
Take a **screenshot** of the video, and let **GPT-4 Vision** tell you what it's about.

---

## 🔥 Features

* 🖐️ Real-time **hand gesture detection** via webcam

  * Fist ✊ → Play / Pause
  * Open Hand ✋ → Volume control / Stop
  * Point 👉 → Seek / Next action
* 🧠 **AI-powered screenshot analysis** with **GPT-4 Vision**
* 🖼️ Capture a screenshot of any YouTube frame with one key (`s`)
* 📄 Get AI explanations directly in your **terminal**
* 🎨 (Planned) **Draw on screen with finger gestures**

---

## ⚙️ Requirements

* Python **3.10+** ✅
* [OpenCV](https://pypi.org/project/opencv-python/)
* [MediaPipe](https://developers.google.com/mediapipe)
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
* [Pillow](https://pypi.org/project/Pillow/)
* [OpenAI Python SDK](https://pypi.org/project/openai/)

---

## 🛠️ Setup Instructions

### 1️⃣ Clone / Open the Project

```bash
git clone https://github.com/Smriti-Prajapati/AirTube.git
cd AirTube
```

If you renamed the folder manually to `AirTube`, just open it in **VS Code** or your IDE.

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

* On **Windows (PowerShell)**:

  ```bash
  .\venv\Scripts\activate
  ```
* On **Linux / MacOS**:

  ```bash
  source venv/bin/activate
  ```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install opencv-python mediapipe pyautogui pillow openai
```

---

### 4️⃣ Add Your OpenAI API Key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

Or set it in your terminal:

```bash
export OPENAI_API_KEY=your_api_key_here   # Linux / MacOS
setx OPENAI_API_KEY "your_api_key_here"   # Windows
```

---

### 5️⃣ Run the Project

```bash
python airtube.py
```

The webcam will start, and you can control YouTube with gestures 🎥.

---

## 🎯 Usage Guide

* **✊ Fist** → Toggle Play / Pause
* **✋ Open Hand** → Volume control (up/down)
* **👉 Pointing** → Seek forward / next
* **`s` key** → Capture screenshot of current frame
* AI explains the frame in **terminal output**

---

## 🚀 Future Enhancements

* 🎨 Finger drawing mode (whiteboard overlay)
* 🎵 Gesture-based **playlist navigation**
* 🗣️ Combine **voice + gesture controls**
* 📊 Stats dashboard for gesture usage

---

## 👩‍💻 Author

Developed with ❤️ by **Smriti Prajapati**

---
