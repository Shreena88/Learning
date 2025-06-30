import json
import os

file_name = "contacts.json"

#Load contacts from file
def load_contacts():
    if os.path.exists(file_name):
        with open(file_name,"r") as f:
            return json.load(f)
    return ()

#save contacts to file
def save_contacts(contacts):
    with open(file_name,"w") as f:
        json.dump(contacts,f,indent=4)

#Create contact
def create_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully.")

#Read contacts
def read_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name,info in contacts.items():
        print(f"Name:  {name}")
        print(f"Phone:  {info['phone']}")
        print(f"Email:  {info['email']}")
        print(f"Address: {info['address']}")

#update contacts
def update_contact(contacts):
    name = input("Enter the name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print("Leave field black to keep current value.")
    phone = input(f"New phone ({contacts[name]["phone"]}): ").strip()
    email = input(f"New email ({contacts[name]["email"]}: ").strip()
    address = input(f"New address ({contacts[name]["address"]}): ").strip()
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address
    print("Contact update successfully!")

#Delete contact
def delete_contact(contacts):
    name=input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

#Search contact
def search_contact(contacts):
    keyword = input("Search bu name: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if keyword in name.lower():
            print(f"Name:  {name}")
            print(f"Phone:  {info['phone']}")
            print(f"Email:  {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("No matching contact.")

#Main function
def main():
    contacts = load_contacts()
    while True:
        print("---Contact book---")
        print("1.Create contact")
        print("2.View all contacts")
        print("3.Search contact")
        print("4.Delete contact")
        print("5.Update contact")
        print("6.Exit")
        choice = input("Enter your choice(1-6): ")

        if choice == "1":
            create_contact(contacts)
        elif choice == "2":
            read_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid option,try again.")

if __name__ == "__main__":
    main()