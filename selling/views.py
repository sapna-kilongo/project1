from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    products=Products.objects.all()
    context={
        'products':products,
    }

    return render(request,'sellingapp/index.html',context)

def check(request,product_id):
    product= Products.objects.get(id=product_id)
    context={
        'product':product,

    }




    return render(request,'sellingapp/product_detail.html',context)  

def loginPage(request):
    return render(request,'sellingapp/login.html')      
    