# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.gis.geos import fromstr
from .models import Apartment,Houses,Hostels,UserProfileInfo
from house_renting_app.forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.measure import Distance,D


# Create your views here.
def index(request):
    if request.method=="POST":
        search_lat=request.POST.get('latitude')
        search_long=request.POST.get('longitude')
        placename=request.POST.get('placename')
        #SRID=4326;POINT (81.84631100000001 25.4358011)
        #search_long=-0.004119873046875001
        #search_lat=0.01270294179045549
        point=fromstr("POINT(%s %s)" %(search_long,search_lat),srid=4326)
        print(point)
        property_type=request.POST.get('property_type')
        print(property_type)
        	#SRID=4326;POINT (-0.004119873046875001 0.01270294179045549)

        if property_type=="Apartment":
            apartment_range = request.POST.get('property_range')
            results=Apartment.objects.filter(location__distance_lt=(point,D(km=apartment_range))).order_by('-rating')

        if property_type=="Hostels":
            apartment_range = request.POST.get('property_range')
            results=Hostels.objects.filter(location__distance_lt=(point,D(km=apartment_range))).order_by('-rating')

        if property_type=="Houses":
            apartment_range = request.POST.get('property_range')
            results=Houses.objects.filter(location__distance_lt=(point,D(km=apartment_range))).order_by('-rating')

        return render(request,'search_results.html',{'results':results,'placename':placename,'property_type':property_type})


    return render(request,'index.html')




def show_apartment(request):
    p_type=request.POST.get('p_type')
    property_id=request.POST.get('property_id')

    if not request.user.is_authenticated:
        return render(request,'modals.html',{'p_type':p_type,'property_id':property_id})  # or http response
    else:
        if(request.method=="POST"):
            # p_type=request.POST.get('p_type')
            # property_id=request.POST.get('property_id')
            print("Hello",p_type,property_id)
            if p_type == "Apartment":
                show=Apartment.objects.get(id=property_id)
                return render(request,'show_apartment.html',{ 'show':show ,'p_type':p_type ,'property_id':property_id })
            if p_type == "Hostels":
                show=Hostels.objects.get(id=property_id)
                return render(request,'show_hostel.html',{'show':show ,'p_type':p_type ,'property_id':property_id})
            if p_type == "Houses":
                show=Houses.objects.get(id=property_id)
                print("Going to Houses")
                return render(request,'show_house.html',{'show':show ,'p_type':p_type ,'property_id':property_id})
            #print("Show",show)

            #return HttpResponse("Error")



def advt_form(request):
    if request.method=="POST":

        property_type=request.POST.get("property_type")

        if(property_type == 'Apartment'):
            print("Hello vaibhava")
            latitude=request.POST.get("latitude")
            longitude=request.POST.get("longitude")
            address=request.POST.get("address")
            apartment_name=request.POST.get("apartment_name")
            apartment_type=request.POST.get("apartment_type")
            super_buildup_area=request.POST.get("super_buildup_area")
            apartment_carpet_area=request.POST.get("apartment_carpet_area")
            apartment_furnishing=request.POST.get("apartment_furnishing")
            apartment_floor_no=request.POST.get("apartment_floor_no")
            apartment_overlooking=request.POST.get("apartment_overlooking")
            apartment_tenants=request.POST.get("apartment_tenants")
            apartment_maintainance_cost=request.POST.get("apartment_maintainance_cost")
            apartment_price=request.POST.get("apartment_price")
            apartment_parking=request.POST.get("apartment_parking")
            apartment_description=request.POST.get("apartment_description")
            img1=request.FILES['img1']
            img2=request.FILES['img2']
            img3=request.FILES['img3']
            apartment_owner_mail=request.POST.get("apartment_owner_email")
            apartment_owner_number=request.POST.get("apartment_owner_number")
            apartment_owner_name=request.POST.get("apartment_owner_name")
            point=fromstr("POINT(%s %s)" %(longitude,latitude),srid=4326)
            data=Apartment(location=point,address=address,apartment_name=apartment_name,
            apartment_type=apartment_type,super_buildup_area=super_buildup_area,
            apartment_furnishing=apartment_furnishing,apartment_floor_no=apartment_floor_no,
            apartment_overlooking=apartment_overlooking,apartment_tenants=apartment_tenants,
            apartment_maintainance_cost=apartment_maintainance_cost,apartment_price=apartment_price,
            apartment_parking=apartment_parking,apartment_description=apartment_description,
            images1=img1,images2=img2,images3=img3,apartment_owner_number=apartment_owner_number,
            apartment_owner_name=apartment_owner_name,apartment_owner_mail=apartment_owner_mail)
            data.save() #here data is the object of the apartmrnt in models
            return render(request,'form_submitted.html')


        #This is for the Hostel type

        if(property_type == 'Hostels'):
            latitude=request.POST.get("latitude")
            longitude=request.POST.get("longitude")
            address=request.POST.get("address")
            hostel_name=request.POST.get("hostel_name")
            hostel_room_size=request.POST.get("hostel_room_size")
            hostel_floor_no=request.POST.get("hostel_floor_no")
            hostel_room_type=request.POST.get("hostel_room_type")
            hostel_attached_bathroom=request.POST.get("hostel_attached_bathroom")
            hostel_mess_facility=request.POST.get("hostel_mess_facility")
            hostel_other_facilities1=True if(request.POST.get("hostel_other_facilities1")) else False
            hostel_other_facilities2=True if(request.POST.get("hostel_other_facilities2")) else False
            hostel_other_facilities3=True if(request.POST.get("hostel_other_facilities3")) else False
            hostel_other_facilities4=True if(request.POST.get("hostel_other_facilities4")) else False
            hostel_price=request.POST.get("hostel_price")
            hostel_description=request.POST.get("hostel_description")
            img4=request.FILES['img4']
            img5=request.FILES['img5']
            img6=request.FILES['img6']
            hostel_owner_mail=request.POST.get("hostel_owner_email")
            hostel_owner_number=request.POST.get("hostel_owner_number")
            hostel_owner_name=request.POST.get("hostel_owner_name")
            point=fromstr("POINT(%s %s)" %(longitude,latitude),srid=4326)
            hostel_data=Hostels(location=point,address=address,hostel_room_size=hostel_room_size,
            hostel_attached_bathroom=hostel_attached_bathroom,hostel_mess_facility=hostel_mess_facility,
            hostel_other_facilities1=hostel_other_facilities1,hostel_other_facilities2=hostel_other_facilities2,
            hostel_other_facilities3=hostel_other_facilities3,hostel_other_facilities4=hostel_other_facilities4,
            hostel_price=hostel_price,hostel_description=hostel_description,images1=img4,images2=img5,images3=img6,hostel_owner_mail=hostel_owner_mail,hostel_owner_name=hostel_owner_name,
            hostel_owner_number=hostel_owner_number)

            hostel_data.save()
            return render(request,'form_submitted.html')

        #This is for the HOUSE type


        if(property_type == 'Houses'):
            print(property_type)
            latitude=request.POST.get("latitude")
            longitude=request.POST.get("longitude")
            address=request.POST.get("address")
            house_no_bedrooms=request.POST.get("house_no_bedrooms")
            house_no_bathrooms=request.POST.get("house_no_bathrooms")
            house_tenants_preffered=request.POST.get("house_tenants_preffered")
            house_carpet_area=request.POST.get("house_carpet_area")
            house_buildup_area=request.POST.get("house_buildup_area")
            house_furnishing=request.POST.get("house_furnishing")
            house_overlooking=request.POST.get("house_overlooking")
            house_floor_no=request.POST.get("house_floor_no")
            house_price=request.POST.get("house_price")
            house_description=request.POST.get("house_description")
            point=fromstr("POINT(%s %s)" %(longitude,latitude),srid=4326)
            img7=request.FILES['img7']
            img8=request.FILES['img8']
            img9=request.FILES['img9']
            house_owner_mail=request.POST.get("house_owner_email")
            house_owner_number=request.POST.get("house_owner_number")
            house_owner_name=request.POST.get("house_owner_name")

            house_data=Houses(location=point,address=address,house_no_bedrooms=house_no_bedrooms,
            house_no_bathrooms=house_no_bathrooms,house_tenants_preffered=house_tenants_preffered,
            house_carpet_area=house_carpet_area,house_buildup_area=house_buildup_area,
            house_furnishing=house_furnishing,house_floor_no=house_floor_no,house_price=house_price,
            house_description=house_description,images1=img7,images2=img8,images3=img9,house_owner_mail=house_owner_mail,house_owner_name=house_owner_name,
            house_owner_number=house_owner_number)

            house_data.save()
            print("Saved")
            return render(request,'form_submitted.html')

    return render(request,'advt_form.html')


#Views for login/Register

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))

@login_required
def special(request):
    return HttpResponse("You are logged in , Nice!")



def register(request):
    registered=False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)  #FIELDS BELONGING TO USERfORM CLASS ARE STORED INTO  user_form object

        print(user_form)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            print("Saved")

        else:
                #Printing the errors
                print(user_form.errors)
    else:
            user_form = UserForm()
            print(user_form)


    return render(request,'modals.html',{'form':user_form})


def get(request):
    return HttpResponseRedirect("Welcome To this Page")

def user_login(request):

    if request.method=="POST":

        username=request.POST.get('username')
        password=request.POST.get('password')

        p_type=request.POST.get('p_type')
        property_id=request.POST.get('property_id')
        #print("login-view",type(p_type),type(property_id))


        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if not property_id:
                return HttpResponse("<h2>Login successfully")
            return render(request,'please_wait.html',{'p_type':p_type,'property_id':property_id})
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            #check="fail"
            #return render(request,'login_check.html',{'check':check})
            return HttpResponse("<h2>Oops !!!You entered wrong credentials</h2>")
    else:
        # return render(request,'index.html')
        return HttpResponseRedirect(reverse('register'))



from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def rating_analysis(request):
    p_type=request.POST.get('p_type')
    property_id=request.POST.get('property_id')
    comment = request.POST.get('comment')

    #p_type,property_id


    #print("Inside rating",property_id,p_type)
    #print(comment)

    #   logic for the sentimental analysis

    client = language.LanguageServiceClient.from_service_account_json('static/sent.json') # Specify the location of the json file...
    document = types.Document(content=comment,type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print(sentiment)

    x = sentiment.score
    a = -1.0
    b = 1.0
    c = 1
    d = 5
    result = (((d-c)*(x-a))/(b-a))+c
    final_rating = round(result,1)
    print("Final Rating",final_rating)

    if p_type=="Apartment":
        data_obj=Apartment.objects.get(id=property_id)
        rating=data_obj.rating
        comments_count=data_obj.comments_count
        print(rating,comments_count)
        total=rating * comments_count
        print("old rating",rating)
        print("Count",comments_count)
        #print(type(final_rating),type(total))
        new_rating=round((final_rating + float(total))/(comments_count+1),1)
        data_obj.rating=new_rating
        data_obj.comments_count+=1
        data_obj.save()
        print("NEw Rating",new_rating)
        print("New rating in table",data_obj.rating)
        print("New Count in table",data_obj.comments_count)
        return render(request,'redirect.html',{'p_type':p_type,'property_id':property_id})
    #return HttpResponseRedirect(reverse('show_apartment',args=(p_type,property_id)))
    print("Above hostel")


    if p_type=="Hostels":
        print("Inside hostels")
        data_obj=Hostels.objects.get(id=property_id)
        rating=data_obj.rating
        comments_count=data_obj.comments_count
        print(rating,comments_count)
        total=rating * comments_count
        print("old rating",rating)
        print("Count",comments_count)
        #print(type(final_rating),type(total))
        new_rating=round((final_rating + float(total))/(comments_count+1),1)
        data_obj.rating=new_rating
        data_obj.comments_count+=1
        data_obj.save()
        print("NEw Rating",new_rating)
        print("New rating in table",data_obj.rating)
        print("New Count in table",data_obj.comments_count)
        return render(request,'redirect.html',{'p_type':p_type,'property_id':property_id})
    #return HttpResponseRedirect(reverse('show_apartment',args=(p_type,property_id)))


    if p_type=="Houses":
        data_obj=Houses.objects.get(id=property_id)
        rating=data_obj.rating
        comments_count=data_obj.comments_count
        print(rating,comments_count)
        total=rating * comments_count
        print("old rating",rating)
        print("Count",comments_count)
        #print(type(final_rating),type(total))
        new_rating=round((final_rating + float(total))/(comments_count+1),1)
        data_obj.rating=new_rating
        data_obj.comments_count+=1
        data_obj.save()
        print("NEw Rating",new_rating)
        print("New rating in table",data_obj.rating)
        print("New Count in table",data_obj.comments_count)
        return render(request,'redirect.html',{'p_type':p_type,'property_id':property_id})
    #return HttpResponseRedirect(reverse('show_apartment',args=(p_type,property_id)))
