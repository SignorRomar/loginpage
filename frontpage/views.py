from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@login_required(login_url='login')

def HomePage(request):
    return render(request, 'frontpage/home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2:  
            return HttpResponse("Passwords don't match!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            '''subject = 'Email Confirmation'
            message = 'This is a confirmation email.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            send_mail(subject, message, from_email, to_email, fail_silently=False)'''
            return redirect('login')

    return render(request, 'frontpage/signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass']
        print(username,pass1)
        user = authenticate(request, username=username, password = pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "Invalid login credentials. Please try again."
        
    return render(request, 'frontpage/login.html', {'error_message': error_message if 'error_message' in locals() else None})

def LogoutPage(request):
    logout(request)
    return redirect('login')


