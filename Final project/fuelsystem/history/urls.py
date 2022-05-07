from django.template.defaulttags import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [

    path('history/', views.history, name='history'),
    path('Logout/', auth_view.LogoutView.as_view(template_name='system/logout.html'), name='Logout'),
]
