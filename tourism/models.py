from django.db import models
from django_jalali.db import  models as jmodels
from django.contrib.auth.models import User






class Customer(models.Model):
    first_name = models.CharField(max_length=100 )
    last_name = models.CharField(max_length=100 )
    password = models.CharField(max_length=100 )
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)



class Agency(models.Model):

    agency_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100 )
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.agency_name



class Tour(models.Model):
    name = models.CharField(max_length=200) 
    price = models.IntegerField()
    last_price = models.IntegerField()
    staying_time = models.CharField(max_length=200)
    trip_type = models.CharField(max_length=200)
    start_date = jmodels.jDateField()
    end_date = jmodels.jDateField()
    start_point = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    agency = models.ForeignKey(Agency,on_delete=models.PROTECT,default=None )
    agency_services = models.CharField(max_length= 300)
    destination_description = models.TextField(max_length=1000 , default = '')
    additional_description = models.TextField(max_length=1000 , default = '')



    def __str__(self) -> str:
        return self.name






class Book(models.Model):

    user = models.ForeignKey(User,on_delete=models.PROTECT,default=None)
    tour = models.ForeignKey(Tour,on_delete=models.PROTECT,default=None)
    number_of_persons = models.IntegerField()
    names_of_persons = models.CharField(max_length= 300)
