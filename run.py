#!/usr/bin/env python3.8
from user import User

def create_user(account_name,user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(account_name,user_name,password)
    return new_user
def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def find_user(user):
    '''
    Function that finds a user by account_name and returns the user
    '''
    return User.find_by_account_name(User)
def check_existing_users(account_name):
    '''
    Function that check if a user exists with that account_name and return a Boolean
    '''
    return User.user_exist(account_name)
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your user list. What is your name?")
    name = input()

    print(f"Hello {name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cu - create a new user, du - display users, fu -find a user, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cu':
                            print("New user")
                            print("-"*10)

                            print ("accountrname ....")
                            account_name = input()

                            print("Last name ...")
                            user_name = input()

                            print("Password ...")
                            password = input()



                            save_users(create_user(account_name,user_name,password)) # create and save new users.
                            print ('\n')
                            print(f"New user {account_name} {user_name} {password}created")
                            print ('\n')

                    elif short_code == 'du':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.account_name} {user.user_name} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

                    elif short_code == 'fu':

                            print("Enter the accountnumber you want to search for")

                            search_account_name = input()
                            if check_existing_users(search_account_name):
                                    search_user = find_user(search_account_name)
                                    print(f"{search_user.first_name} {search_user.user_name}{search_user.password}")
                                    print('-' * 20)

                                    print(f"account_name.......{search_user.account_name}")
                                    print(f"user_name.......{search_user.user_name}")
                                    print(f"password ......{search_user.password}")
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
