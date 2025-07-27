import easyocr
import re

class DocumentAnalyzer:
    def __init__(self):
        self.reader = easyocr.Reader('mn', gpu=True)
    
    def analyze_document(self, image_path):
        result = self.reader.readtext(image_path)
        texts = [item[1] for item in result]
        all_words = []
        for text in texts:
            words = re.findall(r'\w+', text)
            all_words.extend(words)
        numbers = [word for word in all_words if word.isdigit()]
        return {
            "extracted_words": all_words,
            "extracted_numbers": numbers,
            "total_words_found": len(all_words),
            "total_numbers_found": len(numbers)
        }