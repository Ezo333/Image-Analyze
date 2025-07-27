from app.utils.openai import OpenAIClient
from app.functions.file import get_cached_result, set_cached_result, delete_file  

def analyze_image_controller(image_path):
    result = get_cached_result(image_path, 'image')
    if result is None:
        analyzer = OpenAIClient()
        result = analyzer.analyze_image(image_path)
        if not result.get("error"):
            set_cached_result(image_path, result, 'image')
    delete_file(image_path)
    return result
