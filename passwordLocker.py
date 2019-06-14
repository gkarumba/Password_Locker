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