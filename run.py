#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import random
import array


def main():
    print("hello world")

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

def create_user(username, password):
    new_user = User(username, password)
    return new_user
def save_users(self):
    self.save_user()
def find_user(self):
    return User.find_user(self)
def list_users(self):
    return User.user_list()
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
    
    







if __name__ == '__main__':
    main()
