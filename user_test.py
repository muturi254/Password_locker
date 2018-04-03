import unittest
from userp import User
# import pyperclip

class TestUser(unittest.TestCase):
    """test the user class"""
    def setUp(self):
        self.new_user = User('peter', 'muturi', 'petermuturi@gmail.com', 33126755)

    def tearDown(self):
        """clears user fter each test"""
        User.user_list = []

    def test_user_instance(self):
        self.assertEqual(self.new_user.first_name, "peter")
        self.assertEqual(self.new_user.last_name, "muturi")
        self.assertEqual(self.new_user.email, "petermuturi@gmail.com")
        self.assertEqual(self.new_user.Id, 33126755)

    def test_user_save(self):
        '''
        test case to test if credentials objects have been saved
        '''

        self.new_user.save_user()  # save new user
        self.assertEqual(len(User.user_list), 1)

    def test_multiple_user_save(self):

        self.new_user.save_user()
        test_user = User("kevin", "menya", "kevinMenya@gmail.com", 33126759)
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_user_delete(self):
        """ test if delete function works"""
        self.new_user.save_user()
        test_user = User("wesley", "mutwiri", "weseymutwiri@gmail.com", 33126755)
        test_user.save_user()
        self.new_user.delete_user()  # to delete a credentials   object
        self.assertEqual(len(User.user_list), 1)


    def test_finding_user(self):
        """test to check if user is able to be found in a search"""
        self.new_user.save_user()
        test_user = User("wesley", "mutwiri", "weseymutwiri@gmail.com", 33126758)
        test_user.save_user()
        found_user = User.find_user_Id(33126758)
        self.assertEqual(found_user.Id,
                         test_user.Id)

    def user_exist(self):
        self.new_user.save_user()
        test_user = User("james", "muriuki", "jamesmuriuki@gmail.com", 33126760)
        test_user.save_user()
        user_exists_already = User.user_exists("james")
        self.assertTrue(user_exists_already)

    def test_display_all_users(self):
        self.assertEqual(User.display_user(), User.user_list)

    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found contact
    #     '''

    #     self.new_user.save_user()
    #     User.copy_email('33126755')
    #     self.assertEqual(self.new_user.email, pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
