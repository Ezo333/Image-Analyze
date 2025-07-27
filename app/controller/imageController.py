from app.utils.openai import OpenAIClient
from app.functions.file import get_image_hash, load_cache, save_cache, delete_file  

def analyze_image_controller(image_path):
    image_hash = get_image_hash(image_path)
    cache = load_cache()
    if image_hash in cache:
        result = cache[image_hash]
    else:
        analyzer = OpenAIClient()
        result = analyzer.analyze_image(image_path)
        cache[image_hash] = result
        save_cache(cache)
    delete_file(image_path)
    return result
