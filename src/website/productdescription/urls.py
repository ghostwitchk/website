from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views



urlpatterns = [
url(r'^cart/',views.CartPostView.as_view()),
url(r'^cartitems/',views.CartAnotherView.as_view()),
]