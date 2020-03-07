import os
from flask import url_for

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	### swagger specific ###
	SWAGGER_URL = '/swagger'
	API_URL = '/static/swagger.json'
	### end swagger specific ###
