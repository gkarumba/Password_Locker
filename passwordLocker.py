import secrets
import pyperclip
import string

class User:
    """
    Class that generates new instance
    """
    user_list = [] #Empty user list
    
    def __init__(self,idNo,username,password):
        self.id = idNo
        self.user = username
        self.psw = password
    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
        
    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
        
    @classmethod
    def find_by_idNumber(cls,number):
        '''
        Method that takes in a number and returns a user that matches that ID number.
        Args:
            number: ID number to search for
        Returns :
            User that matches the ID number.
        '''
        for user in cls.user_list:
            if user.id == number:
                return user
    
    @classmethod
    def user_exists(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.id == number:
                return True
        return False

    @classmethod
    def match_user_password(cls,username,password):
        '''
        Method that checks if a username && password match.
        Args:
            username & password: username to search if it matches to password
        Returns :
            Boolean: True or false depending if the username && password match
        '''
        for user in cls.user_list:
            if user.user == username:
                user_name = user
                if user_name.psw == password:
                    return True
                return False
        return False
        
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    
class Credentials:
    """
    Class that generates new instance
    """
    cred_list = [] #Empty credentials list
    
    def __init__(self,account,userName,password):
        self.acc = account
        self.userName = userName
        self.credPsw = password
    
    def save_cred(self):
        '''
        save_cred method saves cred objects into cred_list
        '''
        Credentials.cred_list.append(self)
    
    def delete_cred(self):
        '''
        delete_cred method deletes a saved cred from the cred_list
        '''
        Credentials.cred_list.remove(self)
        
    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a Account that matches that name.
        Args:
            name: name to search for
        Returns :
            Account that matches the name.
        '''
        for cred in cls.cred_list:
            if cred.acc == name:
                return cred
            
    @classmethod
    def cred_exists(cls,name):
        '''
        Method that checks if a acc exists from the acc list.
        Args:
            name: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the acc exists
        '''
        for cred in cls.cred_list:
            if cred.acc == name:
                return True
        return False
    
    @classmethod
    def generate_password(cls,length):
        '''
        generate_password method generates passwords for the user cred accounts
        '''
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password
    
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the cred list
        '''
        return cls.cred_list
    
    @classmethod
    def copy_credential_psw(cls,acc_name):
        '''
		Class method that copies a credential password based on the credential name
		'''
        searchCred = Credentials.find_by_name(acc_name)
        return pyperclip.copy(searchCred.credPsw) 
		