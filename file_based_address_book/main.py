from file_handler import read_contacts, write_new_contact, write_whole_contacts
from tabulate import tabulate

while True:
    contacts = read_contacts()

    print("\n1. Add Contact\n2. View all Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\n")
    option = input("Please choose option number: ")

    match option:
        case '1':
            phone = input('Phone: ')

            if any(con['phone'] == phone for con in contacts):
                print('Already exist')
                continue

            name = input('Name: ')
            email = input('Email: ')

            write_new_contact({
                "name": name,
                "phone": phone,
                "email": email
            })
        case '2':
            if not contacts:
                print('No record found')
            else:
                print(tabulate(
                    contacts,
                    headers="keys",
                    tablefmt="grid"
                ))    
        case '3':
            searchedName = input("Please enter name which you want to search: ")
            searchedData = []
            for item in contacts:
                if item['name'].strip().lower()==searchedName.strip().lower():
                    searchedData.append(item)
                print(tabulate(
                    searchedData,
                    headers="keys",
                    tablefmt="grid"
                ))
        case '4':
            searchedName = input("Please enter name which you want to update: ").strip().lower()
            newNumber = input("Please enter new phone number: ").strip()

            updated = False

            for item in contacts:
                if item['name'].strip().lower() == searchedName:
                    item['phone'] = newNumber
                    updated = True

            if updated:
                write_whole_contacts(contacts)
                print('Contact(s) updated successfully')
            else:
                print('No contact found with this name')
        case '5':
            searchedName = input("Please enter name which you want to delete: ")
            updatedContacts = []
            for item in contacts:
                if item['name'].strip().lower()!=searchedName.strip().lower():
                    updatedContacts.append(item)
            write_whole_contacts(updatedContacts)
            print('Contacts deleted sucessfully')
        case '6':
            break    
                    



