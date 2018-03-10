from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()



router.register('singnup', views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name ='login')





urlpatterns = [

url(r'', include(router.urls)),
url(r'^login-user/',views.ReturnLoginUser.as_view())

]
