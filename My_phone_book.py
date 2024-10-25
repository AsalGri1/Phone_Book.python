class Human:
    def __init__(self, firstname, lastname, email, relation=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.relation = relation

    def show_info(self):
        info = f"FirstName: {self.firstname}, LastName: {self.lastname}, Email: {self.email}"
        if self.relation:
            info += f", Relation: {self.relation}"
        return info


class Address:
    def __init__(self, city, street, alley, zipcode):
        self.city = city
        self.street = street
        self.alley = alley
        self.zipcode = zipcode

    def show_address(self):
        return f"{self.city}, {self.street}, {self.alley}, {self.zipcode}"


class Contact(Address):
    def __init__(self, human, phone_number, phone_type, city, street, alley, zipcode):
        super().__init__(city, street, alley, zipcode)
        self.human = human
        self.phone_number = phone_number
        self.phone_type = phone_type

    def show_contact_info(self):
        contact_info = self.human.show_info()
        contact_info += f", Phone: {self.phone_number} (Type: {self.phone_type}), Address: {self.show_address()}"
        return contact_info


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if len(contact.phone_number) != 11:
            print("Error: Phone number must be 11 digits!")
            return
        self.contacts.append(contact)
        print(f"Contact '{contact.human.firstname} {contact.human.lastname}' added successfully!")

    def show_contacts(self):
        if not self.contacts:
            print("PhoneBook is empty:(")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.show_contact_info()}")

    def edit_contact(self, index, firstname=None, lastname=None, email=None, phone_number=None, phone_type=None, city=None, street=None, alley=None, zipcode=None, relation=None):
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact index:(")
            return

        contact = self.contacts[index]
        human = contact.human

        if firstname: human.firstname = firstname
        if lastname: human.lastname = lastname
        if email: human.email = email
        if relation: human.relation = relation

        if phone_number:
            if len(phone_number) != 11:
                print("Error: Phone number must be 11 digits!")
                return
            contact.phone_number = phone_number

        if phone_type: contact.phone_type = phone_type
        if city: contact.city = city
        if street: contact.street = street
        if alley: contact.alley = alley
        if zipcode: contact.zipcode = zipcode

        print(f"Contact '{human.firstname} {human.lastname}' updated successfully!")

    def delete_contact(self, index):
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact index!")
            return
        removed_contact = self.contacts.pop(index)
        print(f"Contact '{removed_contact.human.firstname} {removed_contact.human.lastname}' deleted successfully!")


def phonebook_menu():
    phonebook = PhoneBook()

    while True:
        print("\nPhoneBook Menu:")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            email = input("Enter email: ")
            relation = input("Enter relationship: ")

            city = input("Enter city: ")
            street = input("Enter street: ")
            alley = input("Enter alley: ")
            zipcode = input("Enter zip code: ")
            phone_number = input("Enter phone number (11 digits): ")
            phone_type = input("Enter phone type (1 for Home, 2 for Mobile): ")

            contact = Contact(Human(firstname, lastname, email, relation), phone_number, phone_type, city, street, alley, zipcode)
            phonebook.add_contact(contact)

        elif choice == "2":
            phonebook.show_contacts()

        elif choice == "3":
            phonebook.show_contacts()
            try:
                index = int(input("Enter the contact number to edit: ")) - 1
                firstname = input("Enter new first name (or press Enter to keep current): ")
                lastname = input("Enter new last name (or press Enter to keep current): ")
                email = input("Enter new email (or press Enter to keep current): ")
                relation = input("Enter new relation (or press Enter to keep current): ")

                phone_number = input("Enter new phone number (11 digits, or press Enter to keep current): ")
                if phone_number and len(phone_number) != 11:
                    print("Error: Phone number must be 11 digits!")
                    continue
                
                phone_type = input("Enter new phone type (1 for Home, 2 for Mobile, or press Enter to keep current): ")

                city = input("Enter new city (or press Enter to keep current): ")
                street = input("Enter new street (or press Enter to keep current): ")
                alley = input("Enter new alley (or press Enter to keep current): ")
                zipcode = input("Enter new zip code (or press Enter to keep current): ")

                phonebook.edit_contact(index, firstname=firstname or None, lastname=lastname or None, email=email or None, phone_number=phone_number or None, phone_type=phone_type or None, city=city or None, street=street or None, alley=alley or None, zipcode=zipcode or None, relation=relation or None)
            except ValueError:
                print("Invalid input! Please enter a valid contact number.")

        elif choice == "4":
            phonebook.show_contacts()
            try:
                index = int(input("Enter the contact number to delete: ")) - 1
                phonebook.delete_contact(index)
            except ValueError:
                print("Invalid input! Please enter a valid contact number.")

        elif choice == "5":
            print("Exiting PhoneBook 3 2 1")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    phonebook_menu()
