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