import unittest
from passwordLocker import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Test class that  defines test cases for the credentials class behaviours.
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Credentials('Instagram','Junius','Brutus') # create credentials object
                                   
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.cred_list = []
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.acc,'Instagram')
        self.assertEqual(self.new_cred.userName,'Junius')
        self.assertEqual(self.new_cred.credPsw,'Brutus')
        
    def test_save_cred(self):
        '''
        test_save_cred test case to test if the cred object is saved into
        the cred list
        '''
        self.new_cred.save_cred() # saving the new cred
        self.assertEqual(len(Credentials.cred_list),1)
        
    def test_save_multiple_cred(self):
        '''
        test_save_multiple_cred to check if we can save multiple cred
        objects to our cred_list
        '''
        self.new_cred.save_cred()
        test_cred = Credentials('Twitter','Mary','Aragon')
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),2)
        
    def test_delete_cred(self):
        '''
        test_delete_cred to test if we can remove a cred from our cred list
        '''
        self.new_cred.save_cred()
        test_cred = Credentials('Facebook','Pope','Clement')
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list), 1)
        
    def test_find_cred_by_accountName(self):
        '''
        test to check if we can find a cred by accountName and display information
        '''
        self.new_cred.save_cred()
        test_cred = Credentials('Medium','Ferdinand','Isabella')
        test_cred.save_cred()
        found_cred = Credentials.find_by_name('Medium')
        self.assertEqual(found_cred.acc,test_cred.acc)
    
    def test_cred_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the cred.
        '''
        self.new_cred.save_cred()
        test_cred = Credentials('Medium','Ferdinand','Isabella')
        test_cred.save_cred()
        cred_exists = Credentials.cred_exists('Medium') 
        self.assertTrue(cred_exists) 
        
    def test_copy_password(self):
        '''
        test to check if we can return a copy of the saved password.
        '''
        self.new_cred.save_cred()
        test_cred = Credentials('Medium','Ferdinand','Isabella')
        test_cred.save_cred()
        Credentials.copy_credential_psw('Medium')
        self.assertEqual(pyperclip.paste(),'Isabella')
        pyperclip.paste()
if __name__ == '__main__':
    unittest.main()