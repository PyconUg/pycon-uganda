from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
# Create your views here.


def home19(request):
    context = {}
    template = 'home19.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = '2019/about/about19.html'
    return render(request, template, context)

def schedule(request):
    context = {}
    template = '2019/schedule/schedule19.html'
    return render(request, template, context)

def conduct(request):
    context = {}
    template = '2019/conduct/conduct19.html'
    return render(request, template, context)

def guidelines(request):
    context = {}
    template = '2019/conduct/guidelines.html'
    return render(request, template, context)

def eporting(request):
    context = {}
    template = '2019/conduct/eporting-guidelines/eporting-guidelines.html'
    return render(request, template, context)

def sponsor_us(request):
    context = {}
    template = '2019/sponsor-us/sponsor-us.html'
    return render(request, template, context)

def sponsors(request):
    context = {}
    template = '2019/our-sponsors/sponsors19.html'
    return render(request, template, context)

def register(request):
    context = {}
    template = '2019/register/register19.html'
    return render(request, template, context)

def traveladvice(request):
    context = {}
    template = '2019/travel/travel19.html'
    return render(request, template, context)

def travelguide(request):
    context = {}
    template = '2019/travel/guidance-international-visitors/travel-guide.html'
    return render(request, template, context)


def fin_aid(request):
    context = {}
    template = '2019/financial-assistance/fin-aid19.html'
    return render(request, template, context)

def team(request):
    context = {}
    template = '2019/team/team19.html'
    return render(request, template, context)

def report(request):
    context = {}
    template = '2019/report/report19.html'
    return render(request, template, context)

