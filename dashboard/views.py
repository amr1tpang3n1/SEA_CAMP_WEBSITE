from django.shortcuts import render
from . import models


# Create your views here.

def frontEnd(request):
    frontend_data = models.webInterfaceData.objects.all()
    return render(request, 'index.html', )
