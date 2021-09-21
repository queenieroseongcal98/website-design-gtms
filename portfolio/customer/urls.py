from django.urls import path, include
from . import views

urlpatterns = [
    path('hcustomer/', views.hcustomer, name='hcustomer'),
    path('transaction/', views.transaction, name='transaction'),
    path('feedback/', views.feedback, name='feedback'),
    path('rates/', views.rates, name='rates'),
    path('sender/', views.sender, name='sender'),
    path('receiver/', views.receiver, name='receiver'),
]