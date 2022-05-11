import data

def display(data):
	print("===================== Contact List =====================")
	for contact in data:
		print("Name:", contact["name"]["first_name"], contact["name"]["middle_name"], contact["name"]["last_name"])
		print("Phone:", contact["phone"]["personal"])
		print("------------------------------------------------------")

display(data.contacts)
