import os

os.makedirs('data', exist_ok=True)
PATH = 'file_based_address_book/data/contacts.csv'

if not os.path.exists(PATH):
    with open(PATH, 'w') as file:
        file.write("name,phone,email\n")

def read_contacts():
    contacts = []
    with open(PATH, 'r') as file:
        lines = file.readlines()
    
    for line in lines[1:]:
        name, phone, email = line.strip().split(",")
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })
    return contacts    

def write_new_contact(detail):
    with open(PATH, 'a') as file:
        file.write(f"{detail['name']},{detail['phone']},{detail['email']}\n")
    print('Contact Added sucessfully')


def write_whole_contacts(details):
    with open(PATH, 'w') as file:
        file.write("name,phone,email\n") 
        for item in details:
            file.write(f"{item['name']},{item['phone']},{item['email']}\n")
