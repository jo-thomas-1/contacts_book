import json

# delete all contacts in list
def delete_all():
	confirm = input("Are you sure you want to delete all contacts from contact book [yes / no]: ").lower()
	if confirm == "yes":
		# write to file
		file = open('data.json', 'w')
		json_object = json.dumps([], indent = 4)

		with file as json_file:
			json_file.write(json_object)
		file.close()

		print("All contacts are deleted")
		return 1
	else:
		return 0

# delete single contact in list
def delete_contact(contact_index):
	temp_data = []
	
	# read data from file
	file = open('data.json', 'r')
	with file as json_file:
		temp_data = json.load(json_file)
	file.close()

	# retrive name
	name = temp_data[contact_index]["name"]["name_preffix"] + " " + temp_data[contact_index]["name"]["first_name"] + " " + temp_data[contact_index]["name"]["middle_name"] + " " + temp_data[contact_index]["name"]["last_name"] + " " + temp_data[contact_index]["name"]["name_suffix"]

	confirm = input("Are you sure you want to delete " + name + " from contact book [yes / no]: ").lower()

	if confirm == "yes":
		# delete contact
		temp_data.pop(contact_index)

		# write back to file
		file = open('data.json', 'w')
		json_object = json.dumps(temp_data, indent = 4)

		with file as json_file:
			json_file.write(json_object)
		file.close()

		print(name, "has been deleted from contact book")
		return 1
	else:
		return 0
