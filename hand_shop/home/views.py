from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.db.models import Q
from .models import Category, Product

# Create your views here.

def home(request):
    category = Category.objects.all()
    return render(request, 'home.html', {'category': category})

def product(request, category):
    product = Product.objects.filter(category=category)
    return render(request, 'product.html', {'product': product})


def prod_detail(request, id):
    product = Product.objects.filter(id=id)
    return render(request, 'detail.html', {'product': product})

#-------------start register---------------#
def register(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def signoutView(request):
    logout(request)
    return redirect('login')
#-------------end register---------------#



## search
def searchResult(request):
    posts = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        posts = Product.objects.all().filter(Q(name__contains=query) |
                                            Q(description__contains=query) |
                                            Q(price__contains=query))

    return render(request, 'search.html', {'query': query, 'posts': posts})
## end search
