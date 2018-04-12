from rest_framework import serializers

from . import models


#class Carting(serializers.ModelSerializer):
 #   class Meta:
  #      model=models.Cart
   #     fields = ('id','Quantity')


#class CartSerializer(serializers.ModelSerializer):

 #   """serialiazer for handling the post request for the cart"""
   # connection = serializers.RelatedField(queryset=models.ProductsDiscription.objects.all())

  #  class Meta:
   #     model = models.Cart
    #    fields = ('id', 'UserId', 'ProductId','Quantity',)

    #def create(self, validated_data):
       # print('hi')
        #user_cart = models.Cart(
         #   UserId=validated_data.get('UserId'),
          #  ProductId=validated_data.get('ProductId'),
           # Quantity = validated_data.get('Quantity'),
             #key = models.ProductsDiscription(validated_data.get('ProductId'))

        #)
        #print('lol')
        #print('Cart__name')


class OneSerializer(serializers.ModelSerializer):
     class Meta:
         model=models.Cart
         fields =('Quantity',)


class SecondSerializer(serializers.ModelSerializer):
     cart__Quantity= serializers.IntegerField()
     class Meta :
         model = models.ProductsDiscription
         fields = ('price','category','photos','specification','name','discription','cart__Quantity')


class ThirdSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Cart
        fields = ('ProductId','Quantity','UserId')





class RandomSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Cart
        fields= ('UserId','Quantity')
#