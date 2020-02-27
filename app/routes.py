from app import app
from flask import request
import pprint, json
from app.models import File, get_size

@app.route('/')
@app.route('/index')
def index():
    return "Hello World! Quel fichier voulez vous traiter ?"


@app.route('/files', methods=['POST'])
def upload_file():
	income_file = request.files['file']
	file = File(filename=income_file.filename,
				filetype=income_file.mimetype,
				filesize=get_size(file),
				filecontent=pprint.pformat(income_file.read()))
	return "Done"