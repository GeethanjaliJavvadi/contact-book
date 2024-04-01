#define the function to add a contact to contact book.

def add_contact(contacts, name, number):
    
#Add a new contact to the contacts book.
    
    contacts[name] = number

def search_contact(contacts, name):
    
#Search for a contact in the contacts book.
    
    if name in contacts:
        return f"Name: {name}, Number: {contacts[name]}"
    else:
        return "Contact not found."
    
#define the function to display the contacts

def display_contacts(contacts):

#Display all contacts in the contacts book.
    
    if not contacts:
        print("Contact book is empty.")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")

#define function to delete the contact

def delete_contact(contacts, name):

    if name in contacts:
        del contacts[name]
        print(f"{name} contact has been deleted from the contact book.")
    else:
        print(f"{name} contact not found in the contact book.")
       
    
#define the function to enter the choice

def main():
    contacts = {}

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Delete contact")
        print("5. Quit")

#enter your choice

        choice = input("Enter your choice: ")

#enter the name of the contact and it's number

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            add_contact(contacts, name, number)
            print("Contact added successfully.")
        elif choice == "2":
            name = input("Enter name to search: ")
            result = search_contact(contacts, name)
            print(result)
        elif choice == "3":
            display_contacts(contacts)
        elif choice == "4":
            name = input("Enter name to search: ")
            result = delete_contact(contacts, name)
        elif choice == "5":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()