from rest_framework import serializers
from . import models

class TestSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Cart
        fields = ('userid','productid','quantity')

class SecondTestSerializer(serializers.ModelSerializer):
    cart__quantity = serializers.IntegerField()
    class Meta:
        model = models.Whole
        fields = ('cart__quantity','name','price')


class ThirdTestSerialier(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'