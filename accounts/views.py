from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *
# from .forms import OrderForm
# from .filters import OrderFilter


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()




    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def home(request):
    return render(request, 'accounts/dashboard.html')

def product(request):
    return render(request, 'accounts/product.html')

def customer(request):
    return render(request, 'accounts/customer.html')
# Create your views here.
