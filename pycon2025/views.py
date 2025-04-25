from django.shortcuts import render

# Create your views here.

def home2025(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)
  
def hopin(request):
    context = {"about": "active"}
    template = '2025/hopin.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = '2025/about/about.html'
    return render(request, template, context)

def scheduIe(request):
    context = {}
    template = '2025/schedule/schedule.html'
    return render(request, template, context)

def conduct(request):
    context = {}
    template = '2025/conduct/conduct.html'
    return render(request, template, context)

def guidelines(request):
    context = {}
    template = '2025/conduct/guidelines.html'
    return render(request, template, context)


def speakers(request):
    context = {}
    template = '2025/speakers/speaker_list.html'
    return render(request, template, context)


def eporting(request):
    context = {}
    template = '2025/conduct/eporting-guidelines/eporting-guidelines.html'
    return render(request, template, context)

def sponsor_us(request):
    context = {}
    template = '2025/sponsor-us/sponsor-us.html'  
    return render(request, template, context)

def sponsors(request):
    context = {}
    template = '2025/sponsors/sponsors.html'
    return render(request, template, context)

def register(request):
    context = {}
    template = '2025/register/register.html'
    return render(request, template, context)

def traveladvice(request):
    context = {}
    template = '2025/travel/travel.html'
    return render(request, template, context)

def fin_aid(request):
    context = {}
    template = '2025/fin-aid/fin-aid.html'
    return render(request, template, context)

def team(request):
    context = {}
    template = '2025/team/team.html'
    return render(request, template, context)

def report(request):
    context = {}
    template = '2025/report/report.html'
    return render(request, template, context)
