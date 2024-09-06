from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.TextChoices):
      COMPUTERS='Computers'
      FOOD='Food'
      KIDS='Kids'
      HOME='Home'
      VEHICLES='Vehicles'

class Product(models.Model):
     name = models.CharField(max_length=100,default='',blank=False)
     description = models.TextField(max_length=1000,default='',blank=False)
     price = models.DecimalField(max_digits=11,blank=False,default=0,decimal_places=2)
     brand = models.CharField(max_length=200,default='',blank=False)
     category = models.CharField(max_length=40,blank=False,choices=Category.choices)
     ratings = models.DecimalField(max_digits=3,blank=False,default=0,decimal_places=2)
     stock = models.IntegerField(blank=False,default=0)
     created_at = models.DateTimeField(auto_now_add=True)
     user =  models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

     def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews',null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    rating = models.IntegerField(blank=False,default=0)
    comment = models.TextField(max_length=1000,default='',blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
