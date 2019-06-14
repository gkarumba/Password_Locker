import unittest
from passwordLocker import Credentials

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
        
if __name__ == '__main__':
    unittest.main()