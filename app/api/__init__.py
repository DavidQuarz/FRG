from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from yaml import load, Loader

bp = Blueprint('api', __name__)


SWAGGER_URL = '/swagger'
API_URL = './static/swagger.yaml'

swagger_yml = load(open(API_URL, 'r'), Loader=Loader)

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Quarz API REST FRG",
        'spec':swagger_yml
    }
)

from app.api import api_routes