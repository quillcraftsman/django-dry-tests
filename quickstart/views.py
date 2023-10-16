"""
Example views to use django-dry-tests module
"""
from django.shortcuts import render


def quickstart_view(request):
    """
    Example view to use django-dry-tests
    """
    context = {
        'quickstart': 'Quickstart',
    }
    return render(request, 'quickstart/quickstart.html', context)
