from django.shortcuts import render

def travel_guide(request, year):
    context = {}
    template = f'{year}/travel-guide/travel-guide.html'
    return render(request, template, context)
