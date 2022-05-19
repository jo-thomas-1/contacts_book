from tabulate import tabulate

# display all contacts in basic list mode
def display_all(data):
	temp_data = []
	for i in range(len(data)):
		temp_data.append([i + 1, data[i]["name"]["first_name"] + " " + data[i]["name"]["middle_name"] + " " + data[i]["name"]["last_name"], data[i]["phone"]["personal"]])

	print(tabulate(temp_data, headers=["#", "Name", "Phone"]))