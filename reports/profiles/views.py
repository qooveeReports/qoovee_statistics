from django.shortcuts import render
from profiles.models import Profile

def profiles(request):
    project_users_info = request.user
    return render(request, 'profiles_info.html', {'profiles': project_users_info})


def profiles_info(request, profiles_id):
    profiles = Profile.objects.get(id=profiles_id)
    return render(request, 'detail_profiles.html', {'profile': profiles})
