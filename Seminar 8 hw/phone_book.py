import view

phone_book = []

def get_phone_book() -> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Are you sure about deleting contact {phone_book[id-1][0]}? (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id-1)

def find_contact():
    global phone_book
    find_string = view.input_find()
    not_find = True
    for id, contact in enumerate(phone_book):
        for item in contact:
            if find_string in item.lower():
                not_find = False
                print((id + 1), *contact)
    if not_find:
        print('Nothing found')

def change_contact():
    global phone_book
    id = view.input_change_contact()
    del_contact = phone_book.pop(id)
    id = view.input_new_contact()
    phone_book.append(id)