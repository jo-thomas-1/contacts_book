import json
import display

data = ""
with open('data.json', 'r') as json_file:
	data = json.load(json_file)

while(True):
	command = ""

	print("=========================")
	print("CONTACTS BOOK")
	print("=========================")

	command = input("Enter your command or type help to see list of available commands: ").lower().split()

	# command analysis -----------------------------------------------------------------
	if command[0] == "exit":
		exit()

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

	# command not found
	else:
		print("Entered command is not found.")