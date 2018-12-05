"""template_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from house_renting_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('advt_form/',views.advt_form,name="advt_form"),
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name="logout"),
    path('show_apartment/',views.show_apartment,name="show_apartment"),
    path('rating_analysis',views.rating_analysis,name="rating_analysis"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
