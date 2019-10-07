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

class Image(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/', default='default.png')
    location = models.ForeignKey(Location, on_delete=models.CASCADE,  blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)


    def __str__(self):
        return self.title

    @classmethod
    def todays_images(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos

    @classmethod
    def get_photos(cls):
        photos = cls.objects.all()
        return photos

    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()