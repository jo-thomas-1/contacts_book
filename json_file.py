import json

# function to read data and store to internal variable
def read(file_name):
	data = []
	file = open(file_name, 'r')
	with file as json_file:
		data = json.load(json_file)
	file.close()
	return data

# function to write data to json file
def write(file_name, data):
	file = open(file_name, 'w')
	json_object = json.dumps(data, indent = 4)

	with file as json_file:
		json_file.write(json_object)
	file.close()
	return 1