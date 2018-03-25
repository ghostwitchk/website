from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from . import serializers
from .models import Cart

# Create your views here.
#class ProductsDiscriptionViewset(viewsets.ModelViewSet):
 #   """test view for returning a particular object from the Productdiscription """

  #  """returns the list of the products based on thier categories"""

   # serializer_class = serializers.ProductsDiscriptionSerializer
    #queryset = models.ProductsDiscription.objects.all().filter(category=
    #'ram')
from . import models

#class CartApi(APIView):
   # """adds item to user's cart when post functions is called"""
    #serializer_class = serializers.CartSerializer


    #def post(self,request):

     #   a=serializers.CartSerializer(data=request.data)

      #  if a.is_valid():
           # a.save()


         #   return Response({'message':'j'})
       # else:
          ##    a.errors, status=status.HTTP_400_BAD_REQUEST)


#class CartItems(APIView):
  #  serializer_class = serializers.CartOnlySerializer


   # def get(self,request):
     #   """returns the list of products in user's cart"""
     #   z = int(request.GET.get('q',''))

        #print(type((models.Cart.objects.filter(UserId=z).values('ProductId'))))
       # queryset=(models.Cart.objects.filter(UserId=z).values())
      #  print(queryset)

       # b =models.Cart.objects.filter(key=z).values()
        #print(b)
        #for i in queryset:

             #print(b)
          #d= i.key.all()
         # print(d)
        #this = serializers.OneMoreSerializerList(queryset,many=True)
         #print(this.data)

       # k=[]
       # for i in queryset:
         #   print(i)
        #    p= i.get("ProductId")
          #  print(p)
            #h=i.key.all()

            #print(h)
           # b=models.ProductsDiscription.objects.
          #  print(models.ProductsDiscription.objects.filter(cart__key__id=p))
#
           # k.append(models.ProductsDiscription.objects.filter(connection__id=p))

       # print(k)
       # abc = serializers.CartOnlySerializer(k,many=True)

       # return JsonResponse({'pcartlist':(abc.data)})
        #return Response({'oo':'kl'})


class TestApi(APIView):
    serializer_class = serializers.ThirdSerializer

    def post(self,request):

        z= serializers.ThirdSerializer(data=request.data)

        if z.is_valid():
            z.save()
            return Response({'message':'k'})
        else :
            return Response({'message':'dafaq'})


class SomethingApi(APIView):
    serializer_class = serializers.OneSerializer
    print('looser')

    def get(self,request):
        z= int(request.GET.get('q',''))
        print(z)
        queryset = models.ProductsDiscription.objects.filter(cart__UserId=z).values('price','specification','category',
                                                                                    'discription','photos','name','cart__Quantity')
        print(queryset)

        dekho = serializers.SecondSerializer(queryset,many=True)
        print(dekho.data)

        return Response({'dont':dekho.data})
