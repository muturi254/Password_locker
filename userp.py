import pyperclip

class User:
    """initiaizesan instance of a user"""
    user_list = []
    def __init__(self, first_name, last_name, email, Id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.Id = Id

    def save_user(self):
        self.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def find_user_Id(cls, id):
        '''
        m
        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.Id == id:
                return user

    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls, Id):
        user_found = User.find_user_Id(Id)
        pyperclip.copy(user_found.email)

        return False
    @classmethod
    def user_exists(cls, first_name):
        '''
        method to check if credential exists
        Args:
            name: account_name to be searched
        boolean:
                true or false 
        '''

        for user in cls.user_list:
            if user.first_name == first_name:
                return True
        return False
