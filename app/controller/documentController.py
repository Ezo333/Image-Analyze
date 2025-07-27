from app.utils.document_analyzer import DocumentAnalyzer
from app.functions.file import get_cached_result, set_cached_result, delete_file  

def analyze_document_controller(image_path):
    result = get_cached_result(image_path, 'document')
    if result is None:
        analyzer = DocumentAnalyzer()
        result = analyzer.analyze_document(image_path)
        if not result.get("error"):
            set_cached_result(image_path, result, 'document')
    delete_file(image_path)
    return result
