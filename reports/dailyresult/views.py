from django.shortcuts import render
from .forms import DailyReportForm
from .models import ReportField
from django.contrib.auth.models import User
from profiles.models import Profile
from django.http import HttpResponseRedirect


def add_report(request):
    form = DailyReportForm(request.POST or None)
    if form.is_valid():
    	form = form.save(commit=False)
    	form.user = request.user
        form.save()
        return HttpResponseRedirect(request.path)
    return render(request, 'report_page.html', {'form': form})
