from django.db import models

# Create your models here.


class ProductsDiscription(models.Model):
    """has all the info about all the products"""
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=255,decimal_places=2)
    discription = models.TextField()
    specification = models.TextField()
    photos = models.URLField()



class Cart(models.Model):
    UserId = models.PositiveIntegerField()
    ProductId = models.PositiveIntegerField()
    Quantity = models .PositiveIntegerField()
    Date = models.DateTimeField(auto_now= True)

    key = models.ForeignKey(ProductsDiscription,related_name='connection')
