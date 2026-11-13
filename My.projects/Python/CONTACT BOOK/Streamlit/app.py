import streamlit as st
import re


# CONTACT_BOOK
# ------------

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class Contactbook:

    def __init__(self):
        self.contacts = []

    def validate_phone(self, phone):
        pattern = r"^[6-9]\d{9}$"

        if re.match(pattern, phone):
            return True
        else:
            return False

    def validate_email(self, email):
        val_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(val_email, email):
            return True
        else:
            return False

    def add_contact(self, name, phone, email):

        if self.validate_phone(phone) == False:
            return "Invalid phone number!"

        if self.validate_email(email) == False:
            return "Invalid email!"

        contact = Contact(name, phone, email)
        self.contacts.append(contact)

        return "Contact added successfully!!"

    def view_contacts(self):

        if len(self.contacts) == 0:
            return []

        return self.contacts

    def search_contact(self, name):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():
                return contact

        return None

    def update_contact(self, name, new_phone, new_email):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                if self.validate_phone(new_phone) == False:
                    return "Invalid phone number!"

                if self.validate_email(new_email) == False:
                    return "Invalid email!"

                contact.phone = new_phone
                contact.email = new_email

                return "Contact updated successfully!"

        return "Contact not found."

    def delete_contact(self, name):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                self.contacts.remove(contact)

                return "Contact deleted successfully!"

        return "Contact not found."


# --------------------------------
# CREATE CONTACT BOOK
# --------------------------------

if "book" not in st.session_state:
    st.session_state.book = Contactbook()

book = st.session_state.book


# --------------------------------
# STREAMLIT TITLE
# --------------------------------

st.title("CONTACT BOOK")

st.write("----------------------------")


# --------------------------------
# MENU BUTTONS
# --------------------------------

st.sidebar.header("CONTACT BOOK MENU")

if st.sidebar.button("Add Contact", use_container_width=True):
    st.session_state.choice = "Add Contact"

if st.sidebar.button("View Contacts", use_container_width=True):
    st.session_state.choice = "View Contacts"

if st.sidebar.button("Search Contact", use_container_width=True):
    st.session_state.choice = "Search Contact"

if st.sidebar.button("Update Contact", use_container_width=True):
    st.session_state.choice = "Update Contact"

if st.sidebar.button("Delete Contact", use_container_width=True):
    st.session_state.choice = "Delete Contact"


# Default page
if "choice" not in st.session_state:
    st.session_state.choice = "Add Contact"

choice = st.session_state.choice


# --------------------------------
# 1. ADD CONTACT
# --------------------------------

if choice == "Add Contact":

    st.header("Add Contact")

    name = st.text_input("Enter name")
    phone = st.text_input("Enter phone number")
    email = st.text_input("Enter email")

    if st.button("Add Contact"):

        if name == "" or phone == "" or email == "":
            st.warning("Please fill all fields!")

        else:

            result = book.add_contact(name, phone, email)

            if result == "Contact added successfully!!":
                st.success(result)
            else:
                st.error(result)


# --------------------------------
# 2. VIEW CONTACTS
# --------------------------------

elif choice == "View Contacts":

    st.header("CONTACT LIST")

    contacts = book.view_contacts()

    if len(contacts) == 0:

        st.info("No contacts available.")

    else:

        for contact in contacts:

            st.write("Name:", contact.name)
            st.write("Phone number:", contact.phone)
            st.write("Email:", contact.email)

            st.divider()


# --------------------------------
# 3. SEARCH CONTACT
# --------------------------------

elif choice == "Search Contact":

    st.header("Search Contact")
    name = st.text_input("Enter name")

    if st.button("Search Contact"):

        contact = book.search_contact(name)

        if contact:

            st.success("Contact found!!")

            st.write("Name:", contact.name)
            st.write("Phone:", contact.phone)
            st.write("Email:", contact.email)

        else:

            st.error("Contact not found!!!")


# --------------------------------
# 4. UPDATE CONTACT
# --------------------------------

elif choice == "Update Contact":

    st.header("Update Contact")

    # STEP 1: FIND CONTACT
    st.subheader("1. Find Contact")

    name_to_find = st.text_input(
        "Enter name to find",
        key="name_to_find"
    )

    if st.button("Find Contact"):

        contact = book.search_contact(name_to_find)

        if contact:

            st.session_state.update_contact = contact
            st.success("Contact found!")

        else:

            st.session_state.update_contact = None
            st.error("Contact not found!")


    # STEP 2: UPDATE CONTACT
    if st.session_state.get("update_contact") is not None:

        contact = st.session_state.update_contact

        st.divider()

        st.subheader("2. Update Contact Details")

        new_name = st.text_input(
            "Enter new name",
            value=contact.name,
            key="new_name"
        )

        new_phone = st.text_input(
            "Enter new phone number",
            value=contact.phone,
            key="new_phone"
        )

        new_email = st.text_input(
            "Enter new email",
            value=contact.email,
            key="new_email"
        )

        if st.button("Update Contact"):

            if not book.validate_phone(new_phone):

                st.error("Invalid phone number!")

            elif not book.validate_email(new_email):

                st.error("Invalid email!")

            else:

                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email

                st.success("Contact updated successfully!")

                st.session_state.update_contact = None


# --------------------------------
# 5. DELETE CONTACT
# --------------------------------

elif choice == "Delete Contact":

    st.header("Delete Contact")

    name = st.text_input("Enter name to delete")

    if st.button("Delete Contact"):

        if name == "":
            st.warning("Please enter a name!")

        else:

            result = book.delete_contact(name)

            if result == "Contact deleted successfully!":
                st.success(result)
            else:
                st.error(result)
