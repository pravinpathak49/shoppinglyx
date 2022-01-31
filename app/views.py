from turtle import Vec2D
from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import Product

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        topwears = Product.objects.filter(category='TW')
        return render(request, 'app/home.html', {'bottomwears':bottomwears, 'mobiles':mobiles, 'topwears':topwears})


class ProductDetailView(View):
    def get(self, request, id):
        item = Product.objects.get(pk=id)
        return render(request, 'app/productdetail.html', {'item':item})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
