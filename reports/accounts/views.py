from django.shortcuts import render
from accounts.forms import Registrations
from django.contrib import auth


def register(request):
    user = Registrations(request.POST)
    if user.is_valid():
        save = user.save()
        save.set_password(user.cleaned_data['password'])
        save.save()
        authenticated(request, request.POST.get('username'), request.POST.get('password'))
    return render(request, 'registrations.html', {'form': user})


def authentication(request):
    if request.POST:
        authenticated(request, request.POST.get('username'), request.POST.get('password'))
    return render(request, 'login.html', {})


def authenticated(request, username, password):
    username = username
    password = password
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
