# vending_machine_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('vending-machine/', views.vending_machine, name='vending_machine'),
    path('vending-machine/submit', views.submit_item, name='submit_item'),

]
