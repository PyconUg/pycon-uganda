from django.shortcuts import render

# Create your views here.

def home20(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)
  
def hopin(request):
    context = {"about": "active"}
    template = '2020/hopin.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = '2020/about/about.html'
    return render(request, template, context)

def scheduIe(request):
    context = {}
    template = '2020/schedule/schedule.html'
    return render(request, template, context)

def conduct(request):
    context = {}
    template = '2020/conduct/conduct.html'
    return render(request, template, context)

def guidelines(request):
    context = {}
    template = '2020/conduct/guidelines.html'
    return render(request, template, context)


def speakers(request):
    context = {}
    template = '2020/speakers/speaker_list.html'
    return render(request, template, context)


def eporting(request):
    context = {}
    template = '2020/conduct/eporting-guidelines/eporting-guidelines.html'
    return render(request, template, context)

def sponsor_us(request):
    context = {}
    template = '2020/sponsor/sponsor.html'
    return render(request, template, context)

def sponsors(request):
    context = {}
    template = '2020/our-sponsors/sponsors.html'
    return render(request, template, context)

def register(request):
    context = {}
    template = '2020/register/register.html'
    return render(request, template, context)

def traveladvice(request):
    context = {}
    template = '2020/travel/travel.html'
    return render(request, template, context)

def fin_aid(request):
    context = {}
    template = '2020/financial-assistance/fin-aid.html'
    return render(request, template, context)

def team(request):
    context = {}
    template = '2020/team/team.html'
    return render(request, template, context)

def report(request):
    context = {}
    template = '2020/report/report.html'
    return render(request, template, context)
