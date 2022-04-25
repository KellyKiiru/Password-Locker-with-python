class Credentials:
    
    credentials_list = []
    
    def __init__(self, account, user_name, password):
        self.account = account
        self.user_name = user_name
        self.password = password
        
    def save_credential(self):
        Credentials.credentials_list.append(self)
        
    def find_credential(self):
        pass
    def display_credentials(self):
        pass
    