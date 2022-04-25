class Credentials:
    
    credentials_list = []
    
    def __init__(self, account, user_name, password):
        self.account = account
        self.user_name = user_name
        self.password = password
        
    def save_credential(self):
        Credentials.credentials_list.append(self)
        
    @classmethod    
    def find_credential_by_account(cls, account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def display_credentials(cls):
        return cls.credentials_list
    