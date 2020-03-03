import base64, pprint
from io import StringIO
from flask import request, jsonify

import logging
import boto3
from botocore.exceptions import ClientError

class File:
	
	def __init__(self, file):
		self.name = file.filename
		self.type = file.mimetype
		self.size = get_size(file)

	def __repr__(self):
		return '<File: {}; Type: {}; Size: {}>'.format(self.name, self.type, self.size)

	def txt_content(self, file):
		stream = file.read().decode("utf-8")
		self.content = stream
		return self.content

	def base64_content(self, file):
		image_string = base64.b64encode(file.read())
		image_string = image_string.decode('utf-8')
		self.content = image_string
		return self.content

	def json_content(self, file):
		stream = file.read().decode("utf-8")
		self.content = stream
		return self.content

	def not_supported_file_content(self):
		self.content = "File not valid"
		return self.content

	def to_json(self):
		output = {
			'name' : self.name,
			'type' : self.type,
			'size' : self.size,
			'content' : self.content
		}
		return output

def get_size(fobj):
	if fobj.content_length:
		return fobj.content_length
	try:
		pos = fobj.tell()
		fobj.seek(0, 2)  #seek to end
		size = fobj.tell()
		fobj.seek(pos)  # back to original position
		return size
	except (AttributeError, IOError):
		pass
	    # in-memory file object that doesn't support seeking or tell
	return 0  #assume small enough


def upload_file_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True