from django.db import models
from django.conf import settings

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
    ProductId = models.ForeignKey(ProductsDiscription)
    Quantity = models .PositiveIntegerField()
    Date = models.DateTimeField(auto_now= True)
    class Meta:
        unique_together = ("UserId","ProductId")

  #  key = models.ForeignKey(ProductsDiscription,related_name='connection')
