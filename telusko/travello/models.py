from django.db import models

# Create your models here.
class Destination(models.Model):
    # id : int -- DON'T NEED ID HERE, THE DATABASE WILL ALREADY PROVIDE AN ID TO KEEP TRACK OF THE TABLES
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics') 
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)