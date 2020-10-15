from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'sellingapp/index.html')

def check(request):
    return render(request,'sellingapp/view.html')    
    