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
        
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User('2','Mary','Aragon')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User('3','Pope','Clement')
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)
        
    def test_find_user_by_idNumber(self):
        '''
        test to check if we can find a user by id number and display information
        '''
        self.new_user.save_user()
        test_user = User('2','Ferdinand','Isabella')
        test_user.save_user()
        found_user = User.find_by_idNumber('2')
        self.assertEqual(found_user.user,test_user.user)          
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User('2','Anne','Boleyn')
        test_user.save_user()
        user_exists = User.user_exists('2') 
        self.assertTrue(user_exists)
    
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)
    
if __name__ == '__main__':
    unittest.main()