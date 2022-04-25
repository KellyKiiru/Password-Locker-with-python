class User:
    
    user_list = []
    
    
    def __init__(self, username, password):
        self.username= username
        self.password= password
        
    def save_user(self):
        User.user_list.append(self)
        
    def find_user(self):
        for user in User.user_list:
            if User.self.user_name == User.user.username:
                return user
    def display_users(self):
        pass