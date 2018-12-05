from __future__ import unicode_literals
from django.contrib.gis import admin
from house_renting_app.models import Apartment,Hostels,Houses,UserProfileInfo


class ApartmentAdmin(admin.ModelAdmin):
    list_display=('location','address','apartment_name','apartment_type','super_buildup_area','apartment_carpet_area','apartment_furnishing','apartment_floor_no','apartment_overlooking','apartment_tenants','apartment_maintainance_cost','apartment_price','apartment_parking','apartment_description','apartment_owner_name','apartment_owner_number','apartment_owner_mail','images1','images2','images3','rating','comments_count')

class HostelsAdmin(admin.ModelAdmin):
    list_display=('location','address','hostel_room_size','hostel_floor_no','hostel_room_type','hostel_attached_bathroom','hostel_mess_facility','hostel_other_facilities1','hostel_other_facilities2','hostel_other_facilities3','hostel_other_facilities4','hostel_price','hostel_description','hostel_owner_name','hostel_owner_number','hostel_owner_mail','images1','images2','images3','rating','comments_count')

class HousesAdmin(admin.ModelAdmin):
    list_display=('location','address','house_no_bedrooms','house_no_bathrooms','house_tenants_preffered','house_carpet_area','house_buildup_area','house_furnishing','house_overlooking','house_floor_no','house_price','house_description','house_owner_name','house_owner_number','house_owner_mail','images1','images2','images3','rating','comments_count')
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Apartment,ApartmentAdmin)
admin.site.register(Hostels,HostelsAdmin)
admin.site.register(Houses,HousesAdmin)
