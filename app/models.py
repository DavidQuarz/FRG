class File:
	
	def __init__(self, file):
		self.name = file.filename
		self.type = file.mimetype
		self.size = get_size(file)

	def __repr__(self):
		return '<File: {}; Type: {}; Size: {}>'.format(self.name, self.type, self.size)

	def meta_data(self):
		output = {
			'name' : self.name,
			'type' : self.type,
			'size' : self.size,
			'content' : self.content
		}
		return output

	def txt_content(self):
		self.content = "1"
		return self.content

	def pdf_content(self):
		self.content = "2"
		return self.content

	def csv_content(self):
		self.content = "3"
		return self.content

	def image_content(self):
		self.content = "4"
		return self.content

	def not_supported_file_content(self):
		self.content = "File not valid"
		return self.content

	def to_json(self):
		output = self.meta_data()
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