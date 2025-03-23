from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django. contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
       
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('accounts:profile')
        else:
            form = UserRegistrationForm()
               
    else:
        form = UserRegistrationForm()
    
    return render(request,  'accounts/register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST) # create an instance of the form
        if form.is_valid():
            username = form.cleaned_data.get('username') # get the username
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) # check if user is in the database
            if user is not None: # if user is in the database
                login(request, user) # log the user in
                messages.success(request, f'Welcome back {username}') # welcome message
                return redirect('accounts:profile') # redirect to profile page
        else:
             form = UserLoginForm()
    else:
        form = AuthenticationForm() # create an instance of the form
    return render(request, 'accounts/login.html', {'form': form}) # render the login page  and sends the form to the template 'form' is the name of the template tag and form is the data being sent to the template


def logout_view(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('product_list')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

                


