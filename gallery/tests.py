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

#  Test case for image class
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(place='Nairobi')
        self.location.save()
        self.category = Category(tag='Food')
        self.category.save()
        self.user = User(first_name="John")
        self.user.save()
        self.image = Image(image='imageurl', title='camera', description='capturing device', location = self.location, category = self.category, user = self.user)

    def test_image_instance(self):
        self.assertTrue(isinstance(self.image, Image))


    def test_delete_image_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

# Test case for locations
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(place='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)
