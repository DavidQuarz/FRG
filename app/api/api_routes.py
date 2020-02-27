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

	if file.type in ["text/plain", "text/csv"]:
		file.txt_content(data)
	elif file.type in ["application/pdf", "image/jpeg", "image/png", "image/gif"]:
		file.base64_content(data)
	elif file.type in ["application/json"]:
		file.json_content(data)
	else :
		file.not_supported_file_content()

	reponse = jsonify(file.to_json())
	reponse.status_code = 201
	return reponse