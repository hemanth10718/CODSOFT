def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    while True:
        name = input("Enter name: ")
        if name.isalpha():
            break
        else:
            print(f"Invalid name '{name}'. Please enter only alphabets.")
            
    while True:
        phone_number = input("Enter phone number: ")
        if phone_number.isnumeric():
            break
        else:
            print(f"Invalid phone number '{phone_number}'. Please enter only numbers.")
    
    email = input("Enter email: ")
    address = input("Enter address: ")
       

    contacts.append({
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    })
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

def search_contact(contacts):
    query = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if contact['name'] == query or contact['phone_number'] == query]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    query = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if contact['name'] == query or contact['phone_number'] == query:
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone_number'] = input("Enter new phone number: ") or contact['phone_number']
            contact['email'] = input("Enter new email: ") or contact['email']
            
            while True:
                new_address = input("Enter new address: ") or contact['address']
                if re.match("^[A-Za-z0-9 ]*$", new_address):
                    contact['address'] = new_address
                    break
                else:
                    print(f"Invalid address '{new_address}'. Please enter only alphabets and numbers.")
                    
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    query = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == query or contact['phone_number'] == query:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    contacts = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the contact book. Thank you, have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
