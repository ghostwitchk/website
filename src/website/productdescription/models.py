from django.db import models

# Create your models here.


class Whole(models.Model):
    name = models.CharField(max_length=255)
    mrp = models.FloatField()
    price = models.FloatField()
    photos = models.URLField()
    category = models.CharField(max_length=255)

class Ram(models.Model):
    size = models.CharField(max_length=255)
    speed = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()
    manufacturer = models.CharField(max_length=255)
    key = models.ForeignKey(Whole)

class Processor(models.Model):
    no_of_cores = models.PositiveIntegerField()
    speed = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.TextField()
    key = models.ForeignKey(Whole)


class Cart(models.Model):
    userid = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    productid = models.ForeignKey(Whole)

    class Meta:
        unique_together = ("userid","productid")


