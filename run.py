#!/usr/bin/env python3.6
from userp import User
import pyperclip


def create_user(first_name, last_name, email, Id):
    '''
    Function to create a new User
    '''
    new_user = User(first_name, last_name, email, Id)
    return new_user


def save_user(user):
    '''
    Function to save User
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def find_user(number):
    '''
    Function that finds a user by Id and returns the user
    '''
    return User.find_user_Id(number)


def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()


def check_existing_user(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exists(number)


def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print(
                "Use these short codes : cc - create a new user, dc - display user, fc -find a user, pp - to generate passoword, ll- login, ex -exit the user list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("-"*10)

                    print("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Email address ...")
                    email = input()

                    print("Id ...")
                    Id = input()

                    # create and save new user.
                    save_user(create_user(
                        f_name, l_name, email, Id))
                    print('\n')
                    print(f"New Contact {f_name} {l_name} created")
                    print('\n')

            elif short_code == 'dc':

                    if display_user():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for user in display_user():
                                    print(
                                        f"{ user.Id} ....{user.first_name} {user.last_name} .....{user.email}")

                            print('\n')
                    else:
                            print('\n')
                            print(
                                "You dont seem to have any contacts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the account Id of user you want to search for")

                    search_Id = input()
                    if check_existing_user(search_Id):
                            search_user = find_user(search_Id)
                            print(f"{search_user.first_name} {search_user.last_name}")
                            print('-' * 20)

                            print(f"Id.......{search_user.first_name}")
                            print(f"Id.......{search_user.last_name}")
                            print(f"Id.......{search_user.Id}")
                            print(f"Email address.......{search_user.email}")
                    else:
                            print("That user does not exist")
            elif short_code == 'pp':
                print("enter your pet name")
                pet_name = input().lower()
                print("enter favourite movie")
                fav_movie = input().lower()
                print("how long do you want your password to be")
                pass_length = int(input())
                print("input gg to generate password or cn to cancel")
                code = input().lower()
                if code == "gg":
                    password = pet_name + fav_movie
                    password = list(password)
                    pass1 = password
                    # pass2 = password.reverse()

                    for i in range(0, pass_length):
                        pass1.append(i)
                        pass1.reverse()
                        if len(pass1)>pass_length:
                            del pass1[pass_length:]

                    print(pass1)
                elif code == "cn":
                    print("bye")
                else:
                    print("wrong input")
            
            elif short_code == 'll':
                print("Hello Dear cutomer welcome back ")
                print("enter username")
                user_id = input()
                print("enter Id")
                user_id = input()
                if check_existing_user(user_id):
                    print("welcome home ")
                    print("**"*10)
                    print("**"*10)
                    print("**"*10)
                    print("**"*10)
                    print("**"*10)
                    print("**"*10)
                else:
                    print("user doesnt exist")
                

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print(
                        "I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
