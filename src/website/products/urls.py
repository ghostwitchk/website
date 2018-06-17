from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

#router.register('ProductList', views.ProductsDiscriptionViewset)


urlpatterns = [

url(r'', include(router.urls)),
url(r'^cart/',views.TestApi.as_view()),
url(r'^cartitems/',views.SomethingApi.as_view()),
url(r'^dekho/',views.SomethingElse.as_view())
]