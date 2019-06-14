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