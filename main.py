import json_file
import display
import help
import delete

data = json_file.read('data.json')

while(True):
	command = ""

	print("=========================")
	print("CONTACTS BOOK")
	print("=========================")

	command = input("Enter your command or type help to see list of available commands: ").lower().split()

	# command analysis -----------------------------------------------------------------
	if command[0] == "exit":
		exit()

	# help commands
	elif command[0] == "help":
		help.display_all()

	# ----- display commands -----
	elif command[0] == "display":
		if command[1] == "contacts":
			display.display_all(data)
		elif command[1] == "contact":
			index = int(command[2]) - 1
			if index < len(data):
				display.display_contact(data[index])
			else:
				print("Please enter a valid serial number")
		elif command[1] == "deleted":
			if command[2] == "contacts":
				display.display_all(json_file.read('deleted_data.json'))
			elif command[2] == "contact":
				deleted_data = json_file.read('deleted_data.json')
				index = int(command[3]) - 1
				if index < len(deleted_data):
					display.display_contact(deleted_data[index])
				else:
					print("Please enter a valid serial number")

	# ----- delete commands -----
	elif command[0] == "delete":
		if command[1] == "contacts":
			delete.delete_all()
			data = []
		elif command[1] == "contact":
			index = int(command[2]) - 1
			if index < len(data):
				delete.delete_contact(index)
				data = json_file.read('data.json')
			else:
				print("Please enter a valid serial number")

	# ----- restore commands -----
	# restore deleted contacts
	# restore deleted contact [index number]
	elif command[0] == "restore":
		if command[1] == "deleted":
			if command[2] == "contacts":
				deleted_data = json_file.read('deleted_data.json')
				data = json_file.read('data.json')

				for contact in deleted_data:
					data.append(contact)

				# write back to main file
				json_file.write('data.json', data)

				# write to delete database
				json_file.write('deleted_data.json', [])

				print("All deleted contacts have been restored")

	# command not found
	else:
		print("Entered command is not found.")