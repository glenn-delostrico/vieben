#accounts/views.py
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                #log user in and redirect to settings
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')    

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
            
    else:
        return render(request, 'accounts/register.html')
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required(login_url='/login/')
def settings(request):
    context = Profile.objects.all()
    return render(request, 'accounts/settings.html', {'context': context} )

@login_required(login_url='/login/')
def edit_pictures(request):
    return render(request, 'accounts/edit_pictures.html')