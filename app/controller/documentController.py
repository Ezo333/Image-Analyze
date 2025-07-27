from app.utils.document_analyzer import DocumentAnalyzer

def analyze_document_controller(image_path):
    analyzer = DocumentAnalyzer()
    result = analyzer.analyze_document(image_path)
    return result
