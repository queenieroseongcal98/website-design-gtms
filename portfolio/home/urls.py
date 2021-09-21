from django.contrib import admin
from django.urls import path, include
from . import views

#Django  admin header customization

admin.site.site_header = "GTMS Administration"
admin.site.site_title = "Welcome to GTMS' Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('rates', views.rates, name='rates'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
