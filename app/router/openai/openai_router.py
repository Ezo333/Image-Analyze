from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from app.controller.imageController import analyze_image_controller
from app.functions.file_upload import save_uploaded_file

openai_router = Blueprint('openai', __name__, url_prefix='/openai')

@openai_router.route('/analyze', methods=['POST'])
def analyze_openai():
    file_path, error, status = save_uploaded_file()
    if error:
        return jsonify(error), status
    result = analyze_image_controller(file_path)
    return jsonify(result), 200