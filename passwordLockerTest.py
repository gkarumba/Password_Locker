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

if __name__ == '__main__':
    unittest.main()