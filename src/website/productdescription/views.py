from django.shortcuts import render


# Create your views here.
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from . import models








class CartPostView(APIView):

    serializer_class = serializers.TestSerializer


    def post(self,request):
        a = serializers.TestSerializer(data=request.data)

        if a.is_valid():
            a.save()
            return Response ({'message':'chal gya'})
        else :

            return Response ({'message':'nahi chala'})

class CartAnotherView(APIView):
    serializer_class = serializers.SecondTestSerializer
    def get(self,request):
        z= int(request.GET.get('q',''))

        queryset = models.Whole.objects.filter(cart__userid=z).values('name','cart__quantity')
        print(queryset)
        abc = serializers.SecondTestSerializer(queryset,many=True)
        return Response ({'chal gya':abc.data})