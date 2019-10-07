from django.db import models
import datetime as dt

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()
        
class Category(models.Model):
    tag = models.CharField(max_length =30)

    def __str__(self):
        return self.tag
    
    @classmethod
    def search_by_image_category(cls, search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    place = models.CharField(max_length =30)

    @classmethod
    def search_by_image_location(cls, search_term):
        photos = cls.objects.filter(location__icontains=search_term)
        return photos

    def __str__(self):
        return self.place

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()