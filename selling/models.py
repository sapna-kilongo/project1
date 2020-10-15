from django.db import models

class Products(models.Model):

    device=(
       ('laptops','laptop'),
       ('smartphone','smartphne'),
       ('others','others'),
      )
    quarantee=(
       ('used','used'),
       ('new','new'),
       
      )
    
    name=models.CharField(max_length=200)
    price=models.FloatField()
    quantinty=models.IntegerField()
    category=models.CharField(max_length=100,choices=device, default='laptops')
    NewandUsed=models.CharField(max_length=10,choices=quarantee, default='new')
    image1= models.ImageField()
    image2= models.ImageField()
    image3= models.ImageField()
    def __str__(self):
          return self.name

class Properties(models.Model):
    products=models.ForeignKey(Products, on_delete=models.CASCADE)   
    RAM=models.CharField(max_length=50, default='4GB')
    internal=models.CharField(max_length=100)
    processor=models.CharField(max_length=100)
    Defficiency=models.TextField(max_length=1000)
    