from django.shortcuts import render

from .models import Structure


# Create your views here.
def main_view(request):
    pass
    return render(request, 'constructor_app/index.html', context={})


def landing_view(request):
    pass
    return render(request, 'constructor_app/landing.html', context={})


def show_structure(request):
    pass
    return render(request, 'constructor_app/structure.html', {'department': Structure.objects.all()})
