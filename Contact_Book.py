"""
Contact Book

A simple command-line Contact Book.

Features:
- Add Contacts
- View Contacts
- Search Contact
- Delete Contact

Skills Used:
- Dictionaries
- File Handling
- Loops
- Exception Handling
"""

# 1. Add contact    → name, phone, city
# 2. View all       → show all contacts
# 3. Search contact → find by name
# 4. Delete contact → remove by name
# 5. Quit

contact_book = {}
while True:
    print("\n======= Contact Book =======")
    print("1. Add Contact(name,phone,city)")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")

    try:
      choice = int(input("Enter Choice:"))

      if choice == 1:

        n = int(input("How many entries?:"))

        for i in range(n):
            name = input("Enter Name: ").title()
            phone = input("Enter Phone Number: ")
            city = input("Enter City: ").title()
            
            if len(phone) != 10 or not phone.isdigit():
               print("Invalid Phone Number! Enter a 10-digit number.")
               continue

            contact_book[name] = (phone,city)

            with open("contacts.txt", "w") as file:
              for name, details in contact_book.items():
                file.write(f"name: {name}\nPhone no.: {details[0]}\nCity: {details[1]}")
    
      elif choice == 2:

        print("\n------- Contact List -------")
        with open("contacts.txt", "r") as file:
            for line in file:
             print(line.strip())
    
      elif choice == 3:
       
       cnt_name = input("Enter Name of the Contact:").title()

       if cnt_name in contact_book:
        details = contact_book[cnt_name]
        print(f"Name  : {cnt_name}")
        print(f"Phone : {details[0]}")
        print(f"City  : {details[1]}")
       else:
        print("Contact not found!")
    
      elif choice == 4:
       
       cnt_name = input("Enter Name to delete: ").title()
       if cnt_name in contact_book:
        del contact_book[cnt_name]
        with open("contacts.txt", "w") as file:
            for name, details in contact_book.items():
                file.write(
                   f"Name: {name}\n"
                   f"Phone: {details[0]}\n"
                   f"City: {details[1]}\n\n")
            print("Contact deleted!")
       else:
          print("Contact not found!")
    
      elif choice == 5:
       print("Quitting.........\nThanks for using the contact book! ☺")
       break
      
      else:
         print("Please enter a valid option(1-5).")

    except ValueError:
       print("Please enter the details properly!!")