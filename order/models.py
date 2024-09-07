from django.db import models
from operator import mod
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class OrderStatus(models.TextChoices):
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'

class PaymentStatus(models.TextChoices):
    PAID = 'Paid'
    UNPAID = 'Unpaid'

class PaymentMethod(models.TextChoices):
    COD = 'COD'
    CARD = 'CARD'


class Order(models.Model):
    city = models.CharField(max_length=100,default="",blank=False)
    zip_code = models.CharField(max_length=100,default="",blank=False)
    street = models.CharField(max_length=100,default="",blank=False)
    state = models.CharField(max_length=100,default="",blank=False)
    country = models.CharField(max_length=100,default="",blank=False)
    phone = models.CharField(max_length=100,default="",blank=False)
    total_amount = models.IntegerField(default=0)
    payment_status = models.CharField(max_length=30,choices=PaymentStatus.choices, default=PaymentStatus.UNPAID)
    payment_method = models.CharField(max_length=30,choices=PaymentMethod.choices, default=PaymentMethod.COD)
    order_status = models.CharField(max_length=30,choices=OrderStatus.choices, default=OrderStatus.PROCESSING)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)



class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,related_name='orderitems')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=1)
    name = models.CharField(max_length=100,default="")
