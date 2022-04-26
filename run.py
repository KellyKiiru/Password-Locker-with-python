#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import random
import array


def generate_password():
    max_length = 7

    numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    special_characters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                          '*', '(', ')', '<']

    joined_list = numerals + uppercase_letters + \
        lowercase_letters + special_characters

    rand_digit = random.choice(numerals)
    rand_upper = random.choice(uppercase_letters)
    rand_lower = random.choice(lowercase_letters)
    rand_symbol = random.choice(special_characters)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(max_length - 4):
        temp_pass = temp_pass + random.choice(joined_list)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
    return password

###########################################################


def create_user(username, password):
    new_user = User(username, password)
    return new_user


def save_users(self):
    self.save_user()


def find_user(self):
    return User.find_user(self)


def list_users(self):
    return User.user_list()

def user_exist(user):
    return User.user_exists(user)
###########################################################


def create_credentials(account, user_name, password):
    new_credential = Credentials(account, user_name, password)
    return new_credential


def save_crential(credential):
    credential.save_credential()


def find_credential(account):
    return Credentials.find_credential_by_account(account)


def display_credentials():
    return display_credentials()

def credential_exist(account):
    return Credentials.credential_exist(account)


############################################################


def passwordCreaterandLocker():
    
    while True:
        print("Hi there, welcome to password locker.\n")
        print("Do you have an account with us?")

        confirmation_option = input().lower()
        
        if confirmation_option == 'yes':
            print("That's great, what is your username?\n")
            user_name = input().lower()
            print("Enter your password.\n")
            user_password = input()

            if user_exist(user_name):
                found_user = find_user(user_name)
                print(f"Hi {found_user}. You are currently logged in.")
                
                while True:
                    print("-"*15)
                    print("Use these shortcode to navigate our app.\n")
                    print("cc to create credential; dc to display credentials; fc to find a credential and ex to exit.")
                    
                    short_code = input().lower()
                    
                    if short_code == "cc":
                        print("Continue to create new credential")
                        print("-"*15)
                        account = input("Please enter your social media account eg twitter or instagram:\n").lower()
                        username = input("Input the username associated with the account...\n")
                        print("-"*15)
                        answer = input("would you like an auto generated password?").lower()
                        
                        if answer == 'yes':
                            password = str(generate_password)
                        elif answer == 'no':
                            password = input("Input your preferred password...\n")
                        else:
                            print("Please use the short code.")
                        save_crential(create_credentials(account, user_name, password))
                    elif short_code == 'dc':
                        if display_credentials():
                            print("This is a list of your accounts\n")
                            print("-"*15)
                            for credential in Credentials.credentials_list:
                                print(f" {credential.account}-- {credential.user_name} -- {credential.password} ")
                            print("\n")
                        else:
                            print("Sorry, you have no credentials.")
                    elif short_code == 'fc':
                        find = input("Enter account name you want to find").lower()
                        
                        if credential_exist(find):
                            found_account = find_credential(find)
                            print("\n")
                            print(f"Acc: {found_account.account} {found_account.password}\n")
                            print("\n")
                        else:
                            print("Credential for account cannot be found. \n")
                    elif short_code == 'ex':
                        return
                    else:
                        print("Kindly use the provided shortcodes.\n")
            else:
                print('\n')
                print("User doesn't seem to have an account.\n")
                
        elif confirmation_option == 'no':
                pass              
        


if __name__ == '__main__':
    passwordCreaterandLocker()
