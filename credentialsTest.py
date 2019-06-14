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
        self.new_credentials = Credentials('1','Junius','Brutus') # create credentials object
                             
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
        
if __name__ == '__main__':
    unittest.main()