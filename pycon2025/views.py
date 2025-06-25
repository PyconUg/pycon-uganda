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

def pyladies(request):
    context = {}
    template = '2025/community/pyladies.html'
    return render(request, template, context)
    
def django_girls(request):
    context = {}
    template = '2025/community/django_girls.html'
    return render(request, template, context)

def pyladies_wksp(request):
    context = {
        'title': "Pyladies Open Source Summit",
        'description': "Pyladies Kampala Open Source Summit that will bring together Python enthusiasts and open-source advocates, both new and experienced, for a one-day event aimed at building community and promoting contributions to open source.",
    }
    template = '2025/community/pyladies_wksp.html'
    return render(request, template, context)
def ngombor(request):
    context = {
        'title': 'Pyladies Kampala Open Source Workshop',
        'description': 'PyLadies Uganda is a group of women developers who love the Python programming language.',
    }
    return render(request, '2025/community/ngombor.html', context)
        
