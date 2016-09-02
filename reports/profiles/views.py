from django.shortcuts import render


def index(request):
    project_users_info = request.user
    return render(request, 'profiles_info.html', {'profiles': project_users_info})
