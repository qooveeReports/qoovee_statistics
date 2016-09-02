from django.shortcuts import render
from profiles.models import Profile


def index(request):
    user = Profile.objects.all()
    return render(request, 'index.html', {'user': user})
