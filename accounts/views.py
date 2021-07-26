from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def userlogin(request):
    return HttpResponse('It works')