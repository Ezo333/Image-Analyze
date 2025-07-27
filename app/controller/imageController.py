from app.utils.openai import OpenAIClient

def analyze_image_controller(image_path):
    client = OpenAIClient()
    return client.analyze_image(image_path)
