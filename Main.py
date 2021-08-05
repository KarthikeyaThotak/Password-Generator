from PasswordGenerator import PasswordGenerator
from DataBase import sqldb
import os

print("Welcome to PassGru\n".center(os.get_terminal_size().columns))
User_In = int(input("[1] Sava a new password\n[2] Retrive Password\n[3] Generate a new password\nInput: "))

if User_In == 1:
    website = input("Website URL: ").lower()
    UserName = input("UserName: ").lower()
    Password = input("Password: ").lower()
    sqldb = sqldb(website, UserName, Password)
    sqldb.__addData__()
elif User_In == 2:
    website = input("[+] Please Enter your Website Name: ")
    UserName = "None"
    Password = "None"
    sqldb = sqldb(website, UserName, Password)
    sqldb.__FetchData__()
elif User_In == 3:
    Char = int(input("How many letter do you want in you Password(Ex. 15): "))
    PasswordGenerator.__PasswordGenerate__(Char)
else:
    print("Sorry Worry input")