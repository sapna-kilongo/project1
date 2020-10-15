from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name="index"),
path('product_detail/<str:product_id>/',views.check,name="check"),
path('loginpage/',views.loginPage,name="loginpage"),


]