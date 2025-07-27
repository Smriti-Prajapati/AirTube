import mediapipe as mp
import cv2
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

def detect_gesture(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark
            fingers = []

            # Thumb: compare x (horizontal)
            fingers.append(1 if lm[4].x < lm[3].x else 0)

            # 4 Fingers: compare y (vertical)
            for tip_id in [8, 12, 16, 20]:
                fingers.append(1 if lm[tip_id].y < lm[tip_id - 2].y else 0)

            total = fingers.count(1)

            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if total == 0:
                pyautogui.press("m")
                return "Fist ✊ → Mute"
            elif total == 5:
                pyautogui.press("k")
                return "Open Hand ✋ → Play/Pause"
            elif fingers[1] == 1 and total == 1:
                pyautogui.press("l")
                return "Index 👉 → Forward"
            elif fingers[0] == 1 and total == 1:
                pyautogui.press("j")
                return "Thumb 👈 → Backward"

    return None
