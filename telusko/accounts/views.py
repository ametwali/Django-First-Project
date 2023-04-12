from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse


# THIS IS FOR THE TABLE THATS ALREADY CREATED FOR YOU IN DJANGO FOR USERS, THE TABLE IS CALLED "auth_user"
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if (request.method == "POST"):
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        # If the username & password exist, it will return a User object. 
        # This means that if it does exist, it won't return an empty object (a None object)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
        
        
    else:
        return render(request, "login.html")

def register(request):
    
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if(password1 == password2):       
            
            # You have to check if the user already exists, if so, don't register them a new account
            if(User.objects.filter(username=username).exists()):
                
                #To print to the user
                messages.info(request, "Username Taken")
                return redirect(register)
                
            elif(User.objects.filter(email=email).exists()):
                
                messages.info(request, "Email Taken")
                return redirect(register)
            
            else:
                # Get all the parameters into one object to pass through, in this case its "user"
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                
                # To save the values into the database:
                user.save()
                print('user created')
                
                return redirect('login')
            
        else:
            messages.into(request, 'password not matching...')
            return redirect(register)
            
        #Once saved, we redirect back to the home page
        return redirect('/')
        
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

