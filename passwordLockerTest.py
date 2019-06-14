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
        self.new_user = User('1','Junius','Brutus') # create user object
                             
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.id,'1')
        self.assertEqual(self.new_user.user,'Junius')
        self.assertEqual(self.new_user.psw,'Brutus')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
    
if __name__ == '__main__':
    unittest.main()