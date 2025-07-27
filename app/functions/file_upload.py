import os
from werkzeug.utils import secure_filename
from flask import current_app, request

def save_uploaded_file():
    file = request.files.get('file')
    if not file or file.filename == '':
        return None, {'error': 'No file uploaded'}, 400
    filename = secure_filename(file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    return file_path, None, None