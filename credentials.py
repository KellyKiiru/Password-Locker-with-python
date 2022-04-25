class Credentials:
    
    credentials_list = []
    
    def __init__(self, account, user_name, password):
        self.account = account
        self.user_name = user_name
        self.password = password
        
    def save_credential(self):
        Credentials.credentials_list.append(self)
    @classmethod    
    def find_credential(cls, account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return account
        
    def display_credentials(self):
        pass
    