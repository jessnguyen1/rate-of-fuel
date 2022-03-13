from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.signin,name="signin"),
    path('signin',views.signin,name="signin"),
    path('register',views.register,name="register"),
    path('client',views.client,name="client")
]