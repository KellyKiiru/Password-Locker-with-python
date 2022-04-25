from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):
    
    def setUp(self) -> None:
        self.new_credential = Credentials("facebook", "kellykiiru", "asdf1234")
        
    def test_init(self):
        self.assertEqual(self.new_credential.account,'facebook')
        
        
    def test_create_credential(self):
        self.new_credential = Credentials("facebook", "kellykiiru", "asdf1234")
        self.new_credential.save_credential()
        
    def test_find_credential_by_account(self):
        self.new_credential = Credentials("facebook", "kellykiiru", "asdf1234")
        self.new_credential.save_credential()
        found_account = Credentials.find_credential_by_account('facebook')
        self.assertEqual(found_account.user_name,self.new_credential.user_name)
        
    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
        
if __name__ == '__main__':
    unittest.main()
