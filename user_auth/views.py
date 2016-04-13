from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import RegisterForm
from django.template.context_processors import request
from httplib import responses
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission, User

def register(request):
    
    if request.method == 'POST':
        responses = HttpResponse()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
    # the password verified for the user
           if user.is_active:
               responses.write("User is valid, active and authenticated")
           else:
               responses.write("The password is valid, but the account has been disabled!")
        else:
            responses.write("The username and password were incorrect.")
        return responses
    
    registerForm = RegisterForm() 
    return render(request, 'user_auth/register.html', {'form':registerForm})

    