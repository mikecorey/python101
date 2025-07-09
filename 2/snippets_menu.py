contacts = ['mike', 'matt', 'mark']

def list_contacts():
  print('list contacts')
  print(contacts)

def create_contact():
  print('create a contact')
  print(contacts)

def update_contact():
  print('update a contact')
  print(contacts)

def delete_contact():
  print('delete a contact')
  print(contacts)

def main_menu():
  choice = ''
  while choice.strip() != 'x':
    choice = input('Choose an option:\n\t1. list contacts\n\t2.create a contact\n\t3. update a contact\n\t4. delete a contact.\n\t(or enter x to exit.)\nChoice: ')
    if choice == '1':
      print('list contacts')
      list_contacts()
    elif choice == '2':
      create_contact()
    elif choice == '3':
      update_contact()
    elif choice == '4':
      delete_contact()
    elif choice == 'x':
      break
    else:
      choice = ''
      print('Invalid Choice')
  print('Goodbye')
main_menu()