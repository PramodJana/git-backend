 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from decimal import Decimal

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #we can use CharField and use regex validators to ensure that phone_number actually stores the digits only
    #models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')

    def __str__(self): #This will print out this model
        return self.user.username


# Create your models here.
class Apartment(models.Model):
    location=models.PointField(null=True)
    objects=models.Manager()
    address=models.CharField(max_length=100,null=True)
    apartment_name=models.CharField(max_length=50,null=True)
    apartment_type=models.CharField(max_length=10,null=True)
    super_buildup_area=models.IntegerField(null=True)
    apartment_carpet_area=models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    apartment_furnishing=models.CharField(max_length=20,null=True)
    apartment_floor_no=models.IntegerField(null=True)
    apartment_overlooking=models.CharField(max_length=100,null=True)
    apartment_tenants=models.CharField(max_length=10,null=True)
    apartment_maintainance_cost=models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    apartment_price=models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    apartment_parking=models.BooleanField(default=True)
    apartment_description=models.CharField(max_length=300,null=True)
    apartment_owner_number=models.PositiveIntegerField(null=True,default=0,validators=[MaxValueValidator(9999999999)])
    apartment_owner_mail=models.CharField(max_length=100,null=True)
    images1=models.ImageField(upload_to="images",null=True)
    apartment_owner_name=models.CharField(max_length=100,null=True)
    images2=models.ImageField(upload_to="images",null=True)
    images3=models.ImageField(upload_to="images",null=True)
    rating=models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    comments_count=models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Apartment"

#models for hostel


class Hostels(models.Model):
    location=models.PointField(null=True)
    objects=models.Manager()
    address=models.CharField(max_length=100,null=True)
    hostel_name=models.CharField(max_length=50,null=True)
    hostel_room_size=models.IntegerField(null=True)
    hostel_floor_no=models.IntegerField(null=True)
    hostel_room_type=models.BooleanField(default=True)
    hostel_attached_bathroom=models.BooleanField(default=True)
    hostel_mess_facility=models.BooleanField(default=True)
    hostel_other_facilities1=models.BooleanField(default=True)
    hostel_other_facilities2=models.BooleanField(default=True)
    hostel_other_facilities3=models.BooleanField(default=True)
    hostel_other_facilities4=models.BooleanField(default=True)
    hostel_owner_name=models.CharField(max_length=100,null=True)
    hostel_owner_number=models.PositiveIntegerField(null=True,default=0,validators=[MaxValueValidator(9999999999)])
    hostel_owner_mail=models.CharField(max_length=100,null=True)
    hostel_price=models.DecimalField(null=True,max_digits=10,decimal_places=2,default=Decimal('0.00'))
    hostel_description=models.CharField(max_length=300,null=True)
    images1=models.ImageField(upload_to="images",null=True)
    images2=models.ImageField(upload_to="images",null=True)
    images3=models.ImageField(upload_to="images",null=True)
    rating=models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    comments_count=models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Hostels"
#models for house


class Houses(models.Model):
    location=models.PointField(null=True)
    objects=models.Manager()
    address=models.CharField(max_length=100,null=True)
    house_name=models.CharField(max_length=100,null=True)
    house_no_bedrooms=models.IntegerField(null=True)
    house_no_bathrooms=models.IntegerField(null=True)
    house_tenants_preffered=models.CharField(max_length=10)
    house_carpet_area=models.IntegerField(null=True)
    house_buildup_area=models.IntegerField(null=True)
    house_furnishing=models.CharField(max_length=15)
    house_overlooking=models.CharField(max_length=30)
    house_floor_no=models.IntegerField(null=True)
    house_owner_name=models.CharField(max_length=100,null=True)
    house_owner_number=models.IntegerField(default=0)
    house_owner_mail=models.EmailField(max_length=100,null=True)
    house_price=models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    house_description=models.CharField(null=True,max_length=300)
    images1=models.ImageField(upload_to="images",null=True)
    images2=models.ImageField(upload_to="images",null=True)
    images3=models.ImageField(upload_to="images",null=True)
    rating=models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    comments_count=models.IntegerField(default=0)


    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Houses"
