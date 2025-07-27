from app.utils.document_analyzer import DocumentAnalyzer
from app.functions.file import get_image_hash, load_cache, save_cache, delete_file  

def analyze_document_controller(image_path):
    image_hash = get_image_hash(image_path)
    cache = load_cache()
    if image_hash in cache:
        result = cache[image_hash]
    else:
        analyzer = DocumentAnalyzer()
        result = analyzer.analyze_document(image_path)
        cache[image_hash] = result
        save_cache(cache)
    delete_file(image_path)
    return result
