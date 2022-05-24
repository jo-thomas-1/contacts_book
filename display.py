from tabulate import tabulate

# display all contacts in basic list mode
def display_all(data):
	temp_data = []
	for i in range(len(data)):
		temp_data.append([i + 1, data[i]["name"]["first_name"] + " " + data[i]["name"]["middle_name"] + " " + data[i]["name"]["last_name"], data[i]["phone"][0]["number"]])

	print("\n")
	print(tabulate(temp_data, headers=["#", "Name", "Phone"]))
	print("\n")

# display single contact
def display_contact(contact):
	print("\n")
	print("Name:", contact["name"]["name_preffix"], contact["name"]["first_name"], contact["name"]["middle_name"], contact["name"]["last_name"], contact["name"]["name_suffix"])
	
	if contact["nickname"] != "":
		print("Nickname:", contact["nickname"])

	if contact["phone"] != []:
		print("----- Phone Number -----")
		for number in contact["phone"]:
			print(number["name"], "Phone:", number["number"])

	if contact["e_mail"] != []:
		print("----- E-Mail -----")
		for email in contact["e_mail"]:
			print(email["name"], "Email:", email["mail"])

	if contact["proffesion"] != "":
		print("----- Proffesion -----")
		for job in contact["proffesion"]:
			print(job["name"], ":", job["value"])

	if contact["address"] != []:
		print("----- Address -----")
		for address in contact["address"]:
			print(address["name"], ":", address["value"])

	if contact["important_dates"] != []:
		print("----- Important Dates -----")
		for dates in contact["important_dates"]:
			print(dates["name"], ":", dates["day"], "-", dates["month"], "-", dates["year"])

	if contact["website"] != "":
		print("Website:", contact["website"])

	if contact["social_accounts"] != []:
		print("-----Social Accounts -----")
		for accounts in contact["social_accounts"]:
			print(accounts["name"], ":", accounts["account"])

	if contact["notes"] != "":
		print("----- Notes -----")
		print("Notes:", contact["notes"])
	print("\n")
