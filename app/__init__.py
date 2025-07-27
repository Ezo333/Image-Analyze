from flask import Flask
from app.router.main_router import main_router
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
    app.register_blueprint(main_router)
    return app
