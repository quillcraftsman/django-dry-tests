from django.http import HttpResponseRedirect
from django.shortcuts import render


def index_view(request):
    if request.method == 'GET':
        context = {
            'title': 'Title'
        }
        return render(request, 'demo/index.html', context)
    return HttpResponseRedirect('/')
