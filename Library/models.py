from django.db import models

# Create your models here.

class Book(models.Model):

    title=models.CharField(max_length=30)
    description=models.TextField()

class Laptops(models.Model):

    brand_name=models.CharField(max_length=30)
    model_name=models.CharField(max_length=30)
    user_type=models.CharField(max_length=30,null=True)