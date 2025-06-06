from django.shortcuts import render

def pyladies(request):
    context = {
        'title': 'PyLadies Uganda',
        'description': 'PyLadies Uganda is a group of women developers who love the Python programming language.',
    }
    return render(request, '2025/community/pyladies.html', context)

def django_girls(request):
    context = {
        'title': 'Django Girls Kampala',
        'description': 'Django Girls is a non-profit organization that empowers and helps women to organize free, one-day programming workshops.',
    }
    return render(request, '2025/community/django_girls.html', context)

def pyladies_wksp(request):
    context = {
       title: "Pyladies Open Source Summit",
       description: "Pyladies Kampala Open Source Summit that will bring together Python enthusiasts and open-source advocates, both new and experienced, for a one-day event aimed at building community and promoting contributions to open source.",
    }
    return render(request, '2025/community/pyladies_wksp.html', context)

def ngombor(request):
    context = {
        'title': 'Pyladies Kampala Open Source Workshop',
        'description': 'PyLadies Uganda is a group of women developers who love the Python programming language.',
    }
    return render(request, '2025/community/ngombor.html', context)