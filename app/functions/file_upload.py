import os
from werkzeug.utils import secure_filename
from flask import current_app, request

def save_uploaded_file():
    files = request.files.getlist('file')
    if not files or len(files) == 0 or files[0].filename == '':
        return None, {'error': 'No file uploaded'}, 400
    if len(files) > 1:
        return None, {'error': 'Only one file should be uploaded'}, 400
    file = files[0]
    filename = secure_filename(file.filename)
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    ext = filename.rsplit('.', 1)[-1].lower()
    if ext not in allowed_extensions:
        return None, {'error': 'File should be PNG or JPG'}, 400
    upload_folder = current_app.config['UPLOAD_FOLDER']
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    return file_path, None, None