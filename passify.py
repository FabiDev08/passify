import random
import string
import pyperclip 

GREEN = "\033[32m"
BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"

use_numbers =  True
use_punctuations = True
copy_password = True
password_length = 10

print(r''' ____               _  __       
|  _ \ __ _ ___ ___(_)/ _|_   _ 
| |_) / _` / __/ __| | |_| | | |
|  __/ (_| \__ \__ \ |  _| |_| |
|_|   \__,_|___/___/_|_|  \__, |
                          |___/ ''')
print(" ")

def number_settings():
    global use_numbers

    while True:
            use_numbers_input = input(f"{BLUE}Do{RESET} you want to {BLUE}use numbers{RESET}? [Y/n] ").strip().lower()
           
            if use_numbers_input == "yes" or use_numbers_input == "y":
                use_numbers = True
                break
            elif use_numbers_input == "no" or use_numbers_input == "n":
                use_numbers = False
                break
            elif use_numbers_input == "":
                use_numbers = True
                break
            else:
                print(f"{RED}Invalid option.{RESET} ")
   
def punctuation_settings():
    global use_punctuations

    while True:
            use_punctuations = input(f"{BLUE}Do{RESET} you want to {BLUE}use punctuations{RESET}? [Y/n] ").strip().lower()
           
            if use_punctuations == "yes" or use_punctuations == "y":
                use_punctuations = True
                break
            elif use_punctuations == "no" or use_punctuations == "n":
                use_punctuations = False
                break
            elif use_punctuations == "":
                use_punctuations = True
                break
            else:
                print(f"{RED}Invalid option.{RESET} ")

def copy_password_settings():
     global copy_password

     while True:
            copy_password = input(f"{BLUE}Do{RESET} you want to have the password directly in the {BLUE}clipboard{RESET}? [Y/n] ").strip().lower()

            if copy_password == "yes" or copy_password == "y":
                copy_password = True
                break
            elif copy_password == "no" or copy_password == "n":
                copy_password = False
                break
            elif copy_password == "":
                copy_password = True
                break
            else:
                print(f"{RED}Invalid option.{RESET} ")

def password_length_settings():
    global password_length

    all_characters = string.ascii_letters

    while True:
         password_length = input(f"{BLUE}Enter{RESET} the {BLUE}length{RESET} of your desired password. (Standard length: 12) ")

         if password_length.isdigit():
              password_length = int(password_length)
              break
         elif password_length == "":
              password_length = 12
              break
         else:
              print(f"{RED}Invalid option. Please enter a number.{RESET} ")

    if use_numbers:
         all_characters += string.digits

    if use_punctuations:
        all_characters += string.punctuation

    else:
         all_characters = string.ascii_letters

    create_password(all_characters)
    

def create_password(all_characters):
    global use_numbers
    global use_punctuations

    password = ''.join(random.choices(all_characters, k=int(password_length)))
    print(f"Random password: {GREEN}{password}{RESET}")

    if copy_password:
         pyperclip.copy(password)
         print("Password copied!")

    create_new_password(all_characters)


def create_new_password(all_characters):
    
    while True:
        new_password = input(f"{BLUE}Do{RESET} you want a {BLUE}new Password{RESET} with the same settings? [Y/n] ").strip().lower()

        if new_password == "yes" or new_password == "y":
                create_password(all_characters)
                break
        elif new_password == "no" or new_password == "n":
                break
        elif new_password == "":
                create_password(all_characters)
                break
        else:
            print(f"{RED}Invalid option.{RESET} ")

number_settings()
punctuation_settings()
copy_password_settings()
password_length_settings()