from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import context


def home(request):
    return render(request, 'system/Login.html')


@login_required()
def logout(request):
    return render(request, 'system/logout.html')




@login_required()
def history(request):
    return render(request, 'system/FuelHistory.html')




@login_required()
def quote(request):
    return render(request, 'system/FuelQuoteForm.html')
