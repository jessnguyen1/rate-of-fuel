from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import context

#from .forms import UserProfileForm
#from .forms import UserProfileForm


def home(request):
    return render(request, 'system/Login.html')


@login_required()
def logout(request):
    return render(request, 'system/logout.html')


def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} your account was created successfully')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'system/Register.html', {'form': form})


@login_required()
def history(request):
    return render(request, 'system/FuelHistory.html')

"""""
@login_required()
def profile(request):
    formProfile = UserProfileForm()
    if request.method == 'POST':
        formProfile = UserProfileForm(request.POST)
        if formProfile.is_valid():
            formProfile.save()
    contextS = {'form': formProfile}

    return render(request, 'system/ClientProfileManagement.html', contextS)


@login_required()
def quote(request):
    return render(request, 'system/FuelQuoteForm.html')
"""