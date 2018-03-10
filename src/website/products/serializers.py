from rest_framework import serializers

from . import models


#class Carting(serializers.ModelSerializer):
 #   class Meta:
  #      model=models.Cart
   #     fields = ('id','Quantity')


class CartSerializer(serializers.ModelSerializer):

    """serialiazer for handling the post request for the cart"""
   # connection = serializers.RelatedField(queryset=models.ProductsDiscription.objects.all())

    class Meta:
        model = models.Cart
        fields = ('id', 'UserId', 'ProductId','Quantity',)

    def create(self, validated_data):
        print('hi')


        user_cart = models.Cart(
            UserId=validated_data.get('UserId'),
            ProductId=validated_data.get('ProductId'),
            Quantity = validated_data.get('Quantity'),
            key = models.ProductsDiscription(validated_data.get('ProductId'))

        )
        print('lol')
        print('Cart__name')

        user_cart.save()
        return user_cart

class ProductsDiscriptionSerializer(serializers.ModelSerializer):
    """serializer for the"""
    #connection = CartSerializer(read_only=True,many=True)
    class Meta:
        model = models.ProductsDiscription
        fields = ('id', 'category', 'name', 'price', 'discription', 'specification',
                  'photos',)




class CartListSerializer(serializers.ModelSerializer):
    """serializer for the queryset(abc) for get function"""
   # connection = Carting(read_only=True,many=True)

    class Meta :
        model = models.ProductsDiscription
        fields =('id','category','name','price','discription','specification','photos')
       # fields =('id','Cart_Quantity')
   # id = serializers.IntegerField()
    #category = serializers.CharField(max_length=255)
    #name = serializers.CharField(max_length=255)
    #price = serializers.DecimalField(max_digits=255,decimal_places=2)
    #discription = serializers.StringRelatedField()
    #specification = serializers.StringRelatedField()
    #photos = serializers.URLField()


class CartListSerializer1(serializers.ListSerializer):
    """upar vale ka beta"""
    child = CartListSerializer()
    allow_null =True
    many = True
class CartOnlySerializer(serializers.ModelSerializer):
    connection = CartListSerializer1()

    class Meta:
        model = models.Cart
        fields = ('connection',)
