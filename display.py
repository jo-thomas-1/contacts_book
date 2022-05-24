from tabulate import tabulate

# display all contacts in basic list mode
def display_all(data):
	temp_data = []
	for i in range(len(data)):
		temp_data.append([i + 1, data[i]["name"]["first_name"] + " " + data[i]["name"]["middle_name"] + " " + data[i]["name"]["last_name"], data[i]["phone"][0]["number"]])

	print(tabulate(temp_data, headers=["#", "Name", "Phone"]))

# display single contact
def display_contact(contact):
	print("Name:", contact["name"]["name_preffix"], contact["name"]["first_name"], contact["name"]["middle_name"], contact["name"]["last_name"], contact["name"]["name_suffix"])
	print("Nickname:", contact["nickname"])

	print("----- Phone Number -----")
	for number in contact["phone"]:
		print(number["name"], "Phone:", number["number"])

	print("----- E-Mail -----")
	for email in contact["e_mail"]:
		print(email["name"], "Email:", email["mail"])

	print("Proffesion:", contact["proffesion"]["designation"], contact["proffesion"]["department"], contact["proffesion"]["company"])

	print("----- Address -----")
	for address in contact["address"]:
		print(address["name"], ":", address["value"])

	print("----- Important Dates -----")
	for dates in contact["important_dates"]:
		print(dates["name"], ":", dates["day"], dates["month"], dates["year"])

	print("Website:", contact["website"])

	print("-----Social Accounts -----")
	for accounts in contact["social_accounts"]:
		print(accounts["name"], ":", accounts["account"])

	print("Notes:", contact["notes"])