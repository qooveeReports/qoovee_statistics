from django.shortcuts import render


def add_report(request):
    return render(request, 'report_page.html', {})
