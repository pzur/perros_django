from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .models import *
from .forms import  OrderForm, CreateUserForm
# from .filters import OrderFilter


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'la cuenta ya fue creada' + user)
            return redirect('login')




    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):

     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
            
             

     context = {}
     return render(request, 'accounts/login.html', context)

def home(request):

    return render(request, 'accounts/dashboard.html')

def product(request):
    return render(request, 'accounts/product.html')

def customer(request):
    return render(request, 'accounts/customer.html')
# Create your views here.
