import unittest
from user import User

class TestUser(unittest.TestCase):
    

    def setUp(self):
        self.new_user = User("kelly", "asdf1234")

    def tearDown(self):
        User.user_list = []

    def test_initialization(self):
        self.assertEqual(self.new_user.username, "kelly")
        self.assertEqual(self.new_user.password, "asdf1234")
    def test_save_user(self):
        self.new_user = User("kelly", "asdf1234")   
        self.new_user.save_user()
        
        self.assertEqual(len(User.user_list),1)     


if __name__ == '__main__':
    unittest.main()
