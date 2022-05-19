import data

def display(data):
	for i in range(len(data)):
		print("Sl. No.: ", i + 1)
		print("Name:", data[i]["name"]["first_name"], data[i]["name"]["middle_name"], data[i]["name"]["last_name"])
		print("Phone:", data[i]["phone"]["personal"])
		print("------------------------------------------------------")

# main program

while(True):
	command = ""

	print("=========================")
	print("CONTACTS BOOK")
	print("=========================")

	command = input("Enter your command or type help to see list of available commands: ")

	if command == "display contacts":
		display(data.contacts)
	elif command == "exit":
		exit()