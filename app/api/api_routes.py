from app.api import bp
from flask import jsonify, request, url_for
from app.models import File, get_size
import pprint, os, csv

@bp.route('/')
def api_get_file():
	return "Hello World!"

@bp.route('/files', methods=['POST'])
def api_upload_file():
	data = request.files['file'] or {}
	file = File(data)

	if file.type == "text/plain":
		file.txt_content()
	elif file.type == "application/pdf":
		file.pdf_content()
	elif file.type == "text/csv":
		file.csv_content()
	elif file.type in ["image/jpeg", "image/png", "image/gif"]:
		file.image_content()
	else :
		file.not_supported_file_content()

	reponse = jsonify(file.to_json())
	reponse.status_code = 201
	return reponse