import openai
import base64
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIClient:
    def analyze_image(self, image_path):
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Analyze this image and describe any numbers and text you see."},
                            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_base64}"}
                        ]
                    }
                ],
                max_tokens=300
            )
            return {"result": response.choices[0].message['content']}
        except Exception as e:
            return {"error": str(e)}
