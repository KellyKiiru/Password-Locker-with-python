class User:
    
    user_list = []
    
    
    def __init__(self, username, password):
        self.username= username
        self.password= password
        
    def save_user(self):
        User.user_list.append(self)
    
    @classmethod  
    def find_user(cls, username):
        for user in cls.user_list:
            if user.username == username:
                return user
    @classmethod
    def display_users(self):
        if User.display_users():
            return User.user_list
    @classmethod
    def user_exists(cls,username):
        for user in cls.user_list:
            if user.username == username:
                return True
        return False