import openai
import pyttsx3
from PIL import Image
import base64
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()

def ask_gpt_about_image(image_path, speak=True):
    try:
        with open(image_path, "rb") as img:
            base64_img = base64.b64encode(img.read()).decode("utf-8")

        response = openai.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this YouTube frame."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"}}
                    ]
                }
            ],
            max_tokens=300
        )

        reply = response.choices[0].message.content.strip()
        print(f"\n🔍 GPT says:\n{reply}\n")

        if speak:
            engine.say(reply)
            engine.runAndWait()

        with open("gpt_logs.txt", "a", encoding="utf-8") as log:
            log.write(f"\n[{datetime.now()}] {image_path}:\n{reply}\n")

        return reply

    except Exception as e:
        print("❌ GPT Vision Error:", e)
        return "Error processing image."
