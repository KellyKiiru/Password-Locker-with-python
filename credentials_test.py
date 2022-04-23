from credentials import Credentials
from main import UserAccounts
import unittest

class Tests(unittest.TestCase):
    
    def test_create_account(self):
        
        account1 = UserAccounts('james','12345')
        
        self.assertEqual(account1.login_username,'james')
        
    def test_account_addition(self):
        account1 = UserAccounts('james','12345')
        self.assertEqual()
    


if __name__ == '__main__':
    unittest.main()

