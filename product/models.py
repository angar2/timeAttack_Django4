from django.db import models
from user.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=256, default='')


class Product(models.Model):
    class Meta:
        db_table = "products"

    name = models.CharField(max_length=256, default='')
    img = models.CharField(max_length=256, default='')
    info = models.CharField(max_length=256, default='')
    price = models.IntegerField(default='')
    stock = models.IntegerField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class OrderStatus(models.Model):
    class Meta:
        db_table = "orderStatus"

    status = models.CharField(max_length=256, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductOrder(models.Model):
    class Meta:
        db_table = "productOrder"

    count = models.IntegerField(default='')
    product = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)


class UserOrder(models.Model):
    class Meta:
        db_table = "userOrder"

    address = models.CharField(max_length=256, default='')
    order_time = models.DateTimeField(default='')
    total_price = models.IntegerField(default='')
    paid_price = models.IntegerField(default='')
    discount_rate = models.FloatField(default='')
    expiration = models.BooleanField(default='')
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)