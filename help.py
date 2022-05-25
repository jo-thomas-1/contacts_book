help_data = [
		{
			"command": "display contacts",
			"description": "Display all contacts stored in contact book."
		},
		{
			"command": "display contact [contact_number]",
			"description": "To display single contact." +
				"\n\t\t[contact_number]: sl. no. or index number of the contact to be displayed."
		},
		{
			"command": "exit",
			"description": "To close the contact book."
		}
	]


def display_all():
	print("\n")
	print("----- HELP SYSTEM -----\n")

	for i in range(len(help_data)):
		print("Command:", help_data[i]["command"])
		print("Description:", help_data[i]["description"], "\n")

	print("\n")