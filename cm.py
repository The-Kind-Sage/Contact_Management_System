print ("\n\n\n [   ~  WELCOME TO CONTACT MANAGER  ~   ] \n ****************************************")
print ("\n Dear user,\n You have different options to begin with. ")
print("\n \n Options:\n -------\n ")
print(" 1. Add Contact\n 2. Update Contact \n 3. Delete Contact\n 4. View Contacts\n 5. Exit")
   
contacts={}

while True:
    choice=input(" \n\n Kindly Enter Your Choice: ")
    
    if choice=="1":
            
            name=input("Enter Contact Name: ")
            no=int(input("Enter Contact Number: "))
            contacts[name] = no
            print(f"\nContact '{name}' added successfully! \n")
    elif choice=="2":
            
                updt=input("Enter the name of the contact to update:")
                if updt in contacts:
                    ncn=int(input("Enter new contact number: "))
                    contacts[updt] = ncn
                                   
                    print(f"\n Contact '{updt}' updated  successfully! \n")
            
                else:
                    print(f"\n No contact found with the name '{updt}'.")
            
    elif choice=="3":
             
                deln=input("Enter the name of the contact to delete:")
            
                if deln in contacts:
                    del contacts[deln]
                    print(f"\n Contact '{deln}' deleted successfully! \n")
            
                else:
                    print(f"\nNo contact found with the name '{deln}'.")
            
    elif choice=="4":
        if contacts:
              print("\n Your Contacts: " )
              print(" --------------\n")
              for name, no in contacts.items():
                  print(f"[ Name:{name}, Phone No:{no} ]")
        else:
            print("You have no contacts")
            
    elif choice=="5":
        print("\n Exiting Contact Manager, Have a wonderful day ahead :)")
        print(" ***************************************************")
        break
    else:
        print("\n Invalid Choice. You only have options between 1 to 5.")     
        

