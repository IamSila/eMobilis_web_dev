from django.shortcuts import render

# Create your views here.
# write functions here

def home(request):
    return render(request, 'home.html')