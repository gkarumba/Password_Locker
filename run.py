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

def main():
    
    
    
if __name__ == '__main__':
    main()