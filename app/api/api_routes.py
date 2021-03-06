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
	buckets = s3.list_buckets()
	bucket_FRG = 'bucket-frg'
	
	existing_bucket = False
	for bucket in buckets['Buckets']:
		if bucket_FRG == bucket["Name"]:
			existing_bucket = True

	if not existing_bucket:
		s3.create_bucket(Bucket=bucket_FRG, CreateBucketConfiguration={'LocationConstraint':'eu-west-1'})

	file_to_s3 = BytesIO(json.dumps(Response.get_json(reponse), sort_keys=True, indent=4).encode('utf-8'))
	
	s3.upload_fileobj(file_to_s3, bucket_FRG, file.name+'.json')

	return reponse