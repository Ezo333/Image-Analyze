from flask import Blueprint
from app.router.openai.openai_router import openai_router
from app.router.freeModel.document_router import document_router

main_router = Blueprint('main', __name__, url_prefix='/main')
main_router.register_blueprint(openai_router)
main_router.register_blueprint(document_router)