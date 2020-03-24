import base64, csv, pprint, json
from collections import OrderedDict
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

	def csv_content(self, file):
		stream = file.read().decode("utf-8")
		csv_content = [{k: v for k, v in row.items()} for row in csv.DictReader(stream.splitlines(), skipinitialspace=True)]
		self.content = csv_content
		return self.content

	def json_content(self, file):
		stream = file.read().decode("utf-8")
		self.content = json.loads(stream, object_pairs_hook=OrderedDict)
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
