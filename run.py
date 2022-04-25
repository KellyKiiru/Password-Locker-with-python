#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import random
import array


def main():
    print("hello world")


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





if __name__ == '__main__':
    main()
