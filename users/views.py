from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProductForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                print(user, 'User create succsessfully.')
                return redirect('products')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match.'
        })


def listProducts(request):
    return render(request, 'products.html')


def createProducts(request):
    if request.method == 'GET':
        return render(request, 'create_product.html', {
            'form': ProductForm()
        })
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.producer = request.user
            new_product.save()
            return redirect('listproducts')
        else:
            return render(request, 'create_product.html', {
                'form': form,
                'error': 'There was an error in the form.'
            })


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm(),
        })
    else:
        User = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if User is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'sername or password is incorrect.'
            })
        else:
            login(request, User)
            return redirect('listproducts')


def signut(request):
    logout(request)
    return redirect('home')
