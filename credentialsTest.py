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
        Credentials.credentials_list = []
        
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.acc,'Instagram')
        self.assertEqual(self.new_cred.userName,'Junius')
        self.assertEqual(self.new_cred.credPsw,'Brutus')
        
if __name__ == '__main__':
    unittest.main()