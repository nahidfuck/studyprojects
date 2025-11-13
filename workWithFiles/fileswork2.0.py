contacts = []

with open("contacts.txt", "r") as file:
    for line in file:
        eline = line.strip().split(", ")
        contacts.append({"name": eline[0], "number": eline[1]})

print("Contacts loaded successfully.")

while True:
    mode = input("Enter your command:\na - add contact\nd - delete contact\ns - search contact\nq - quit\n")
    if mode == "q":
        print("Exiting program.")
        break
    elif mode == "s":
        seekname = input("Enter name to search: ")
        for contact in contacts:
            if contact["name"] == seekname:
                print(f"Found contact: {contact['name']}, {contact['number']}")
                break
        else:
            print("Contact not found.")
    elif mode == "a":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts.append({"name": name, "number": number})
        with open("contacts.txt", "a") as file:
            file.write(f"{name}, {number}\n")
        print("Contact saved successfully.")
    elif mode == "d":
        