from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from app.controller.imageController import analyze_image_controller

routes = Blueprint('routes', __name__)

@routes.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        result = analyze_image_controller(file_path)
        return jsonify(result), 200
    return jsonify({'error': 'File upload failed'}), 500
