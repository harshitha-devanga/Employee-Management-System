from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('index/',views.index),
    path('viewemployee/',views.viewemployee,name='viewemployee'),
    path('addemployee/',views.addemployee,name='addemployee'),
    path('delete/<int:pk>',views.deleteemployee,name='deleteemployee'),
    path('edit/<int:pk>',views.editemployee,name='editemployee')
]
