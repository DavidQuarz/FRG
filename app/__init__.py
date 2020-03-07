from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.api import SWAGGERUI_BLUEPRINT, SWAGGER_URL
### swagger specific ###
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app.main import routes
from app import models