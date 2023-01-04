import phone_book as pb


def main_menu():
    print('Choose menu command: ')
    print('1. Show phonebook ')
    print('2. Load phonebook ')
    print('3. Save phonebook ')
    print('4. Add contact ')
    print('5. Change contact ')
    print('6. Delete contact ')
    print('7. Find contact ')
    print('0. Exit app \n')
    return input_menu()


def input_menu():
    while True:
        try:
            choice = int(input('Enter menu option: '))
            if choice in range(1, 8) or choice == 0:
                return choice
            else:
                print('There is no such menu option')
        except:
            print('Input error. Put in the correct menu option')


def print_phone_book():
    phone_book = pb.get_phone_book()
    print()
    if len(phone_book) < 1:
        print('Phonebook is empty or not loaded\n')
    else:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    print()

def input_new_contact():
    name = input('input contact name ')
    phone = input('input contact phone ')
    comment = input('input comment ')
    new_contact = [name, phone, comment]
    return new_contact

def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('input contact ID, which you need to delete: '))
    return id

def input_change_contact():
    print()
    print_phone_book()
    id = int(input('input contact ID, which needs to be changed: '))
    return id

def input_find():
    find = input('Input search: ').lower()
    return find