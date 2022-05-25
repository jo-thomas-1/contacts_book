import json
import display
import help
import delete

# function to read data and store to internal variable
def read_data():
	data = []
	file = open('data.json', 'r')
	with file as json_file:
		data = json.load(json_file)
	file.close()
	return data


data = read_data()

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

	# display commands
	elif command[0] == "display":
		if command[1] == "contacts":
			display.display_all(data)
		elif command[1] == "contact":
			index = int(command[2]) - 1
			if index < len(data):
				display.display_contact(data[index])
			else:
				print("Please enter a valid serial number")

	# delete commands
	elif command[0] == "delete":
		if command[1] == "contacts":
			delete.delete_all()
			data = []
		elif command[1] == "contact":
			index = int(command[2]) - 1
			if index < len(data):
				delete.delete_contact(index)
				data = read_data()
			else:
				print("Please enter a valid serial number")


	# command not found
	else:
		print("Entered command is not found.")