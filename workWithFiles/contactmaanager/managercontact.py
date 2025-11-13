import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent = 2)

contacts = load_contacts()

print("Contacts loaded successfully.")

while True:
    mode = input("Enter command:\nhelp, add, list, search, edit, delete, exit\n")
    
    if mode == 'exit':
        print("Exiting program.")
        break

    elif mode == 'help':
        print("Available commands:")
        print("help - Show this help message")
        print("add - Add a new contact")
        print("list - List all contacts")
        print("search - Search for a contact by name")
        print("edit - Edit an existing contact")
        print("delete - Delete a contact")
        print("exit - Exit the program\n")

    elif mode == 'add':
        name = input("Enter contact name: ").strip()
        number = input("Enter contact number: ").strip()
        duplicate = False
        for c in contacts:
            if c["number"] == number:
                duplicate = True
                break

        if duplicate:
            print("This phone number already exists. Contact not added.")
            continue
        contacts.append({"name": name, "number": number})
        save_contacts(contacts)
        print("Contact added successfully.")

    elif mode == 'list':
        if not contacts:
            print("No contacts found.")
            continue
        else:
            print("Your contacts:")
            for contact in contacts:
                print(f"{contact['name']}, {contact['number']}")

    elif mode == 'search':
        seekname = input("Enter name to search: ").strip().lower()
        matches = []

        for c in contacts:
            if seekname in c["name"].lower():
                matches.append(c)

        if matches:
            print(f"Found {len(matches)} match(es):")
            for c in matches:
                print(f"{c['name']}, {c['number']}")
        else:
            print("Contact not found.")
    elif mode == 'edit':
        edit_number = input("Enter the name of the contact to edit: ").strip()
        for c in contacts:
            if c["name"].lower() == edit_number.lower():
                new_name = input("Enter new name (leave blank to keep current): ")
                new_number = input("Enter new number (leave blank to keep current): ")
                if new_name:
                    c["name"] = new_name
                if new_number:
                    c["number"] = new_number
                save_contacts(contacts)
                print("Contact updated successfully.")
                break
        else:
            print("Contact not found.")
    elif mode == 'delete':
        del_number = input("Enter the name of the contact to delete: ").strip()
        for i, c in enumerate(contacts):
            if c["name"].lower() == del_number.lower():
                contacts.pop(i)
                save_contacts(contacts)
                print("Contact deleted successfully.")
                break
        else:
            print("Contact not found.")