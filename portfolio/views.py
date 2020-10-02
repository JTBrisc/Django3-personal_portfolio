from django.shortcuts import render
from .models import Project


def home(request):
    # Grab the elements out of the DB
    projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {'projects':projects})


