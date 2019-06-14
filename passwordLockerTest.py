import unittest
# import pyperclip
from passwordLocker import User

class TestUser(unittest.TestCase):
    '''
    Test class that  defines test cases for the user class behaviours.
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user('1'Junius','Brutus') # create user object