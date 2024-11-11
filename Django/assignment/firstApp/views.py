from django.shortcuts import render

# Create your views here.
def index(request):
    """defines the context and renders the request"""
    name = "sila Mulingi"
    context = {
        "name": name,
        "phone_number": 123456676,
        "age": 45
    }
    return render(request, "index.html", context)
