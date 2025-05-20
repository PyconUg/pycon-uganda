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