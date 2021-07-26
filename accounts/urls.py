from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.userlogin, name='userlogin'),
    path('signup/', v.usersignup, name='usersignup'),
]
