from operator import imod
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
        
if __name__ == '__main__':
    unittest.main()
