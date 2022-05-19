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

	command = input("Enter your command or type help to see list of available commands: ").lower()

	if command == "display contacts":
		display.display_all(data)
	elif command == "exit":
		exit()