import json


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }


class ContactManager:

    def __init__(self):
        self.contacts = []
        self.load_contacts()


    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contact = Contact(name, phone, email)
        self.contacts.append(contact)

        self.save_contacts()
        print("Contact added successfully!")


    def view_contacts(self):
        if not self.contacts:
            print("No contacts found")
            return

        for contact in self.contacts:
            print("----------------")
            print("Name:", contact.name)
            print("Phone:", contact.phone)
            print("Email:", contact.email)


    def search_contact(self):
        name = input("Enter name to search: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact found:")
                print("Phone:", contact.phone)
                print("Email:", contact.email)
                return

        print("Contact not found")


    def update_contact(self):
        name = input("Enter contact name to update: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():

                contact.phone = input("New phone: ")
                contact.email = input("New email: ")

                self.save_contacts()
                print("Contact updated!")
                return

        print("Contact not found")


    def delete_contact(self):
        name = input("Enter contact name to delete: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():

                self.contacts.remove(contact)
                self.save_contacts()

                print("Contact deleted!")
                return

        print("Contact not found")


    def save_contacts(self):
        data = [contact.to_dict() for contact in self.contacts]

        with open("contacts.json", "w") as file:
            json.dump(data, file)


    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)

                for contact in data:
                    self.contacts.append(
                        Contact(
                            contact["name"],
                            contact["phone"],
                            contact["email"]
                        )
                    )

        except FileNotFoundError:
            pass



manager = ContactManager()


while True:

    print("""
===== Contact Management System =====

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        manager.add_contact()

    elif choice == "2":
        manager.view_contacts()

    elif choice == "3":
        manager.search_contact()

    elif choice == "4":
        manager.update_contact()

    elif choice == "5":
        manager.delete_contact()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")