#This will be the main part of our program where we can choose
#which function we want to use.

from file_access import *
from generate import *


def run_main_menu():

    #we will run this menu until a user decides to exit
    while True:

        print("Please select a menu option by entering its number: ")
        print("1: Generate New Password")
        print("2: Recover Password")
        print("3: Exit")
        user_selection = input("Selection: ")

        if user_selection == "1":
            #generate password
            continue
        elif user_selection == "2":
            #recover password
            continue
        elif user_selection == "3":
            print("Exiting")
            break
        else:
            print("Selection",user_selection, "is not an option")
