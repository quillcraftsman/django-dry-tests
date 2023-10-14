"""
Views for test main features
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .models import Simple


def index_view(request):
    """
    View for list and greate object
    :param request:
    :return:
    """
    if request.method == 'GET':
        context = {
            'title': 'Title'
        }
        return render(request, 'demo/index.html', context)

    # name = request.POST.get('name', None)
    # if name is not None:
    #     Simple.objects.create(name=name)
    return HttpResponseRedirect('/')


def param_view(request, kwarg):
    """
    view to test params and kwargs in url
    :param reqeust:
    :param kwarg:
    :return:
    """
    a_param = request.GET.get('a')
    b_param = request.GET.get('b')
    context = {
        'a': a_param,
        'b': b_param,
        'kwarg': kwarg,
    }
    return render(request, 'demo/index.html', context)


# def one_view(request, pk):
#     """
#     One view with pk to detail, update and delete object
#     :param request:
#     :param pk:
#     :return:
#     """
#     return render(request, 'demo/index.html')
