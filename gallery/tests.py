from django.test import TestCase
import datetime as dt
from .models import User, Location, Category, Image


# Test case for User class
class UserTestClass(TestCase):
    def setUp(self):
        self.user = User(first_name = "John", last_name="Muriuki", email = "hidalie@gmail.com", phone_number="0722334455")
        self.user.save()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_delete_user_method(self):
        self.user.save_user()
        users = User.objects.all()
        self.user.delete_user()
        users = User.objects.all()
        self.assertTrue(len(users) == 0)
