import data
import display

while(True):
	command = ""

	print("=========================")
	print("CONTACTS BOOK")
	print("=========================")

	command = input("Enter your command or type help to see list of available commands: ").lower()

	if command == "display contacts":
		display.display_all(data.contacts)
	elif command == "exit":
		exit()