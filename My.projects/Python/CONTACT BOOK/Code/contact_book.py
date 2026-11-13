#  CONTACT_BOOK
# --------------

import re

class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email

class Contactbook:
    def __init__(self):
        self.contacts=[]

    
    def validate_phone(self,phone):
        pattern=r"^[6-9]\d{9}$"
        if re.match(pattern,phone):
            return True
        else:
            return False

    
    def validate_email(self,email):
        val_email=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(val_email,email):
            return True
        else:
            return False

   
    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        if self.validate_phone(phone) == False:
            print("Invalid phone number!")
            return

        email = input("Enter email: ")

        if self.validate_email(email) == False:
            print("Invalid email!")
            return

        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added successfully!!")


    def view_contacts(self):
        if len (self.contacts)==0:
            print("no contacts avilable")
            return
        
        print("\n-----CONTACT LIST-----")
        print("\n-----------------------")

        for contact in self.contacts:
            print("Name:",contact.name)
            print("Phone number:",contact.phone)
            print("Email:",contact.email)
            return
        
  
    def search_contact(self):
        name=input("enter name:")
        for contact in self.contacts:
            if contact.name.lower()==name.lower():
                print("contact found!!")
                print("name:",contact.name)
                print("phone:",contact.phone)
                print("email:",contact.email)
            else:
                print("contact not found!!!")

    def update_contact(self):
        name = input("Enter name to update: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():

                new_phone = input("Enter new phone number: ")

                if self.validate_phone(new_phone) == False:
                    print("Invalid phone number!")
                    return

                new_email = input("Enter new email: ")

                if self.validate_email(new_email) == False:
                    print("Invalid email!")
                    return

                contact.phone = new_phone
                contact.email = new_email

                print("Contact updated successfully!")
                return

        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter name to delete: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return

        print("Contact not found.")

book = Contactbook()

while True:

    print("\n----------------------------")
    print("       CONTACT BOOK")
    print("----------------------------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book.add_contact()

    elif choice == "2":
        book.view_contacts()

    elif choice == "3":
        book.search_contact()

    elif choice == "4":
        book.update_contact()

    elif choice == "5":
        book.delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice!")