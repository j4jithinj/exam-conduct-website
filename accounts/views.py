from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'accounts/login.html', {})

def usersignup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        email = request.POST.get('email')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        password = request.POST.get('password')
        user = User.objects.create_user(email, email, password)
        user.firs_tname = firstname
        user.last_name = lastname
        user.save()
        return redirect('userlogin')
    return render(request, 'accounts/signup.html', {'form':form})

def userlogout(request):
    logout(request)
    return redirect('userlogin')

@login_required(login_url='userlogin')
def profile(request):
    return render(request, 'accounts/dashboard.html')