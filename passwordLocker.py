class User:
    """
    Class that generates new instance
    """
    user_list = [] #Empty user list
    
    def __init__(self,username,password):
        self.user = username
        self.psw = password
    