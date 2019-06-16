!#/usr/bin/env python3.6
from passwordLocker import User

def create_user(id,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(id,username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a user by ID number and returns the user
    '''
    return user.find_by_number(number)

def check_existing_users(number):
    '''
    Function that check if a user exists with that ID number and return a Boolean
    '''
    return user.user_exists(number)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return user.display_users()

def login_user(username,password):
    '''
    Function that returns all the saved users
    '''
    return user.match_user_password(username,password)

def main():
    print("Hello Welcome to your Password_Locker. Proceed to create your account")
    print("New User")
    print("-"*10)
    print ("Username ....")
    username = input()
    print ("Password ....")
    password = input()
    id  = len(User.user_list) + 1
    save_contact(create_contact(id,username,password))
    print('\n')
    while True:
        print(f"{username}. Please log in")
        print ("Password ....")
        pass_word = input()
        login_user(username,pass_word)
        if login_user():
            print("Use these short codes : ca - create a new account, da - display accounts, fc -find an account, ex -exit the user list ")
        short_code = input().lower()
        if short_code == 'cc':
            print("New Contact")
            print("-"*10)
            print ("First name ....")
            f_name = input()
            print ("Last name ....")
            l_name = input()
            print ("Phone number ....")
            phone = input()
            print ("Email address ....")
            e_address = input()
            save_contact(create_contact(f_name,l_name,phone,e_address))
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print ('\n')
        elif short_code == 'dc':
            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')
                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')
        elif short_code == 'fc':
            print("Enter the number you want to search for")
            search_number = input()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 20)
                print(f"Phone number.......{search_contact.phone_number}")
                print(f"Email address.......{search_contact.email}")
            else:
                print("That contact does not exist")
        elif short_code == 'ex':
            print('Bye ...........')
        else:
            print("I really didn't get that. Please use the short codes")
    
    
if __name__ == '__main__':
    main()