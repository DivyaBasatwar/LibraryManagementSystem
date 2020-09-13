from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=50,default="anonymous")
    email = models.EmailField(default='sample@sample.com')
    category = models.CharField(max_length=50,default="")
    description = models.TextField(default="Very Good Book")

    def __str__(self):
        return self.name
