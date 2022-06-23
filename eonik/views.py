from django.shortcuts import render

def index(request):

    context = {
        'title': 'Eonik',
    }

    return render(request, 'eonik/index.html', context)
