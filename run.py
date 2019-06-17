#!/usr/bin/env python3.6
from passwordLocker import User, Credentials

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
    return User.match_user_password(username,password)

def create_account(account,userName,password):
    '''
    Function to create a new account
    '''
    new_acc = Credentials(account,userName,password)
    return new_acc

def save_acc(acc):
    '''
    Function to save acc
    '''
    acc.save_cred()

def del_acc(acc):
    '''
    Function to delete acc
    '''
    acc.delete_cred()

def find_acc(name):
    '''
    Function that finds an account and returns the account
    '''
    return Credentials.find_by_name(name)

def check_existing_acc(name):
    '''
    Function that check if an acc exists with that name and return a Boolean
    '''
    return Credentials.cred_exists(name)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()

def copy_password(name):
    '''
    Function that copies a specific account's password
    '''
    return Credentials.copy_credential_psw(name)

def main():
    print("Welcome to your Password_Locker. Proceed to create your account")
    print("New User")
    print("-"*10)
    print ("Username ....")
    username = input()
    print ("Password ....")
    password = input()
    id  = len(User.user_list) + 1
    save_user(create_user(id,username,password))
    print('\n')
    while True:
        print(f"Welcome {username}. To continue please log in")
        print ("Password ....")
        pass_word = input()
        # login_user(username,pass_word)
        if login_user(username,pass_word):
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, cc -copy the password, ex -exit the cred list ")
            short_code = input().lower()
            if short_code == 'ca':
                print("New Account")
                print("-"*10)
                print ("Account name ....")
                acc_name = input()
                print ("User Name ....")
                userName = input()
                print ("Enter preffered password length ....")
                pswLength = int(input())
                password = Credentials.generate_password(pswLength)
                save_acc(create_account(acc_name,userName,password))
                print('\n')
                print(f"New Account for {acc_name} with the username: {userName} has been created successfully")
                print ('\n')
            elif short_code == 'da':
                if display_accounts():
                    print("Here is a list of all your accounts")
                    print('\n')
                    for account in display_accounts():
                        print(f"{account.acc} {account.userName} .....{account.credPsw}")
                        print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any accounts saved yet")
                    print('\n')
            elif short_code == 'fa':
                print("Enter the account name you want to search for")
                search_name = input()
                if check_existing_acc(search_name):
                    search_account = find_acc(search_name)
                    print(f" Account Name:{search_account.acc}")
                    print('-' * 20)
                    print(f"Username.......{search_account.userName}")
                    print(f"Account Password.......{search_account.credPsw}")
                else:
                    print("That Account does not exist")
            elif short_code == 'cc':
                print("Enter the account name you want to copy the password")
                copy_psw = input()
                if check_existing_acc(copy_psw):
                    password_copy = copy_password(copy_psw)
                    print(f"Password for {copy_psw} has been copied")
                    print('-' * 20)
                else:
                    print("That Account does not exist")
            elif short_code == 'ex':
                print('You are now exiting the app ...........')
            else:
                print("I really didn't get that. Please use the short codes")
        else:
            print('Username and password do not match.Please try again ') 
if __name__ == '__main__':
    main()