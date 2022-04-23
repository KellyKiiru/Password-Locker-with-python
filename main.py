class UserAccounts:
    
    accounts = []
    
    def __init__(self, username, password):
        self.login_username = username
        self.account_password = password
    
    
    
account1 = UserAccounts ("kelly", '12345zxcvb')

print(account1.account_password)
    