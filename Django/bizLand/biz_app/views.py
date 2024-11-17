from django.shortcuts import render
from .models import Company
from .models import Team
# Create your views here.


def index(request):
    context = {'companies' : Company.objects.all(), 'team': Team.objects.all()}

    return render(request, 'index.html', context )
