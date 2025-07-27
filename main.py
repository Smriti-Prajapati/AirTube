import cv2
import time
import os
import pyttsx3
from gesture_utils import detect_gesture
from ai_helper import ask_gpt_about_image

cap = cv2.VideoCapture(0)
engine = pyttsx3.init()
os.makedirs("screenshots", exist_ok=True)

print("🟢 AirTube Running... (Press 's' to take screenshot, 'q' to quit)")

last_gesture_time = 0
gesture_delay = 1.5  # seconds
last_screenshot_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    if current_time - last_gesture_time > gesture_delay:
        action = detect_gesture(frame)
        if action:
            print(f"🖐️ Detected: {action}")
            cv2.putText(frame, action, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            last_gesture_time = current_time

    cv2.imshow("AirTube 🎯", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and (current_time - last_screenshot_time > 2):
        filename = f"screenshots/frame_{int(current_time)}.jpg"
        success = cv2.imwrite(filename, frame)
        if success:
            print("📸 Screenshot saved:", filename)
            engine.say("Screenshot captured. Sending to GPT.")
            engine.runAndWait()

            print("📤 Sending to GPT...")
            try:
                response = ask_gpt_about_image(filename)
                print("🤖 GPT Response:", response)
            except Exception as e:
                print("❌ GPT Error:", e)
        else:
            print("⚠️ Failed to save screenshot.")
        last_screenshot_time = current_time

    elif key == ord('q'):
        print("👋 Exiting AirTube...")
        break

cap.release()
cv2.destroyAllWindows()
