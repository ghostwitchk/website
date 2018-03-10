from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from rest_framework import status
from . import models
from rest_framework.response import Response
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer


from django.http import JsonResponse
from django.http import HttpResponse
import json



# Create yur views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creating reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
     """checks email and password and returns an auth token"""
     serializer_class = AuthTokenSerializer

     def create(self,request):
         """use the ObtainAuthToken apiview to validate and create a token"""
         return(ObtainAuthToken().post(request))

#     def retrieve(self, request, pk=None):
#         z= request.GET.get('q','')
#         queryset = models.UserProfile.objects.filter(email=z).values()
#         return Response({'user':list(queryset)})
#class LoginApi(APIView):


class ReturnLoginUser(APIView):
    #serializer_class = serializers.LoginUserSerializer

    def get(self,request):
        z= request.GET.get('q','')
        print(z)

        print(models.UserProfile.objects.filter(email=z))

        queryset = models.UserProfile.objects.all().filter(email= z).values()
        print(queryset)
        # print(person)

        return JsonResponse({'name':list(queryset)})
