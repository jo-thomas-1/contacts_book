from tabulate import tabulate

# display all contacts in basic list mode
def display_all(data):
	temp_data = []
	for i in range(len(data)):
		temp_data.append([i + 1, data[i]["name"]["first_name"] + " " + data[i]["name"]["middle_name"] + " " + data[i]["name"]["last_name"], data[i]["phone"]["personal"]])

	print(tabulate(temp_data, headers=["#", "Name", "Phone"]))

# display single contact
def display_contact(contact):
	print("Name:", contact["name"]["name_preffix"], contact["name"]["first_name"], contact["name"]["middle_name"], contact["name"]["last_name"], contact["name"]["name_suffix"])