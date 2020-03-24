from app.api import bp
from flask import jsonify, request, Response, url_for
from app.models import File
import pprint, os, csv, json, boto3
from io import BytesIO

@bp.route('/')
def api_get_file():
	return "Hello World"

@bp.route('/files', methods=['POST'])
def api_upload_file():
	data = request.files['file'] or {}
	file = File(data)

	content_accepted = True

	if file.type in ["text/plain"]:
		file.txt_content(data)
	elif file.type in ["text/csv"]:
		file.csv_content(data)
	elif file.type in ["application/pdf", "image/jpeg", "image/png", "image/gif"]:
		file.base64_content(data)
	elif file.type in ["application/json"]:
		file.json_content(data)
	else :
		file.not_supported_file_content()
		content_accepted = False

	reponse = jsonify(file.to_json())
	if content_accepted:
		reponse.status_code = 201
	else :
		reponse.status_code = 415


	#Stockage du fichier json dans S3
	s3 = boto3.client('s3')
	s3.upload_fileobj(BytesIO(json.dumps(Response.get_json(reponse), sort_keys=True, indent=4).encode('utf-8')), 'bucketdemarde', file.name+'.json')

	return reponse