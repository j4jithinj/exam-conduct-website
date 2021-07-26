from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def userlogin(request):
    return render(request, 'accounts/login.html', {})

def usersignup(request):
    form = UserCreationForm(request.POST or None)
    return render(request, 'accounts/signup.html', {'form':form})