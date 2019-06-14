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