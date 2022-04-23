from contextlib import ContextDecorator


class UserAccounts:
    '''
    This class provides the blueprint for creating instances of UserAccount objects'''
    
    accounts = []
    
    def __init__(self, username, password):
        '''
        this sets the attributes of the account'''
        self.login_username = username
        self.account_password = password
    
    def addAccounts():
        '''
        this adds accounts to an accounts list'''
        initial_response = input("hi, would you like to create a credential's account? \n If so, press y; If not, press n\n")
        
        if initial_response == 'y':
            social_media_platform = input("What social media platform do you want to create a credentials account for?\n. f for Facebook, t for Twitter, i for Instagram \n")
            
            
            
            
            if social_media_platform == social_media_platform.lower():
                username = input("What is your username?\n")
                password = input("Input the password you want to save\n")

                new_account = UserAccounts(username, password)
                
                def addaccount(self):
                    contacts = contacts.append(new_account)
                
        else:
            print('We feel that you could benefit from our services. Kindly reconsider and give us a try at a later date. Bye')

    addAccounts()