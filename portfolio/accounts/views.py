from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def signup(request):
    #return HttpResponse ("This is my about page (/about)")
    return render(request, 'accounts/signup.htm')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']   

        if password1==password2:
            if User.objects.filter(username=username).exists():
                #print('Username is already taken!')
                messages.warning(request, 'Username is already taken!', extra_tags='alert') 
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                #print('This email is already taken!')
                messages.warning(request, 'Email is already taken!', extra_tags='alert') 
                return redirect('register')

            else:    
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,)
                user.save()
                #print('user created')
                return redirect('login')

        else:
            #print('Password do not match.. Please try again!')
            messages.warning(request, 'Password do not match!', extra_tags='alert') 
            return redirect('register')
        
        messages.success(request, 'Your account was created successfully!', extra_tags='alert')
        return redirect('register')

    else:
        return render(request, 'accounts/register.htm')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            #print('You are logged in.')
            return redirect('hcustomer')

        else:
            messages.warning(request, 'Invalid Credentials.', extra_tags='alert') 
            return redirect('login')

    else:
        return render(request, 'accounts/login.htm')

def logout(request):
    auth.logout(request)
    return redirect('home')