from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from app.controller.documentController import analyze_document_controller
from app.functions.file_upload import save_uploaded_file

document_router = Blueprint('document', __name__, url_prefix='/document')

@document_router.route('/analyze', methods=['POST'])
def analyze_document():
    file_path, error, status = save_uploaded_file()
    if error:
        return jsonify(error), status
    result = analyze_document_controller(file_path)
    return jsonify(result), 200