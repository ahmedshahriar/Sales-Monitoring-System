"""bd_map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
app_name = "bd_map"

urlpatterns = [
    path('', views.index, name='index'),
    path('map',views.map,name='map'),
    path('upload',views.upload,name='upload'),
    path('top_sales',views.top_sales,name='top_sales'),
    path('top_changed_sales_areas',views.top_changed_sales,name='top_changed_sales'),
]
