import os

# Get the directory where the user wants to store contacts
directory = input("\n\n\nBefore Opening Contact Manager,\nType the location of your file where you want to manage your contacts: ")
if os.path.exists(directory):
    file_path = os.path.join(directory, "contacts.txt")
    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        open(file_path, "w").close()  # Create an empty file
else:
    print("Location does not exist")
    import sys
    sys.exit()
    
    
    
        
print ("\n\n\n [   ~  WELCOME TO CONTACT MANAGER  ~   ] \n ****************************************")
       
# Menu options
print("\n Dear user,\n You have different options to begin with. ")
print("\n Options:\n -------\n ")
print(" 1. Add Contact\n 2. Update Contact \n 3. Delete Contact\n 4. View Contacts\n 5. Exit \n")


# Function to read all contacts from the file
def read_contacts():
    contacts = {}
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():  # Skip empty lines
                name, phone = line.strip().split(", ")
                contacts[name] = phone
    return contacts

# Function to write all contacts back to the file
def write_contacts(contacts):
    with open(file_path, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}, {phone}\n")


# Main program loop
while True:
    choice = input(" \n\nNow, select an option to continue: ")

    if choice == "1":  # Add Contact
        name = input("Enter Contact Name: ").strip()
        phone = input("Enter Contact Number: ").strip()

        contacts = read_contacts()
        if name in contacts:
            print(f"\nContact '{name}' already exists. Use the update option to modify it.")
        else:
            contacts[name] = phone
            write_contacts(contacts)
            print(f"\nContact '{name}' was added successfully.")

    elif choice == "2":  # Update Contact
        name = input("Enter the name of the contact to update: ").strip()

        contacts = read_contacts()
        if name in contacts:
            new_phone = input("Enter new contact number: ").strip()
            contacts[name] = new_phone
            write_contacts(contacts)
            print(f"\nContact '{name}' was updated successfully.")
        else:
            print(f"\nNo contact found with the name '{name}'.")

    elif choice == "3":  # Delete Contact
        name = input("Enter the name of the contact to delete: ").strip()

        contacts = read_contacts()
        if name in contacts:
            del contacts[name]
            write_contacts(contacts)
            print(f"\nContact '{name}' was deleted successfully.")
        else:
            print(f"\nNo contact found with the name '{name}'.")

    elif choice == "4":  # View Contacts
        contacts = read_contacts()
        if contacts:
            print("\n Your Contacts: \n--------------")
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone Number: {phone}")
        else:
            print("No contacts found.")

    elif choice == "5":  # Exit
        print("\n Exiting Contact Manager, Have a wonderful day ahead :)")
        print(" ***************************************************")
        break

    else:
        print("\n Invalid Choice. You only have options between 1 to 5.")
        
            