from django.db import models

# Create your models here.
class Products(models.Model):

    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    discount_per = models.BigIntegerField()
    price = models.BigIntegerField()
    mrp_price = models.BigIntegerField()
    color = models.CharField(max_length=50)
    model_item = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)

class Order(models.Model):

    def __str__(self):
        return self.name
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=100)
    total = models.CharField(max_length=200)