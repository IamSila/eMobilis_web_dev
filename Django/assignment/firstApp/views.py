from django.shortcuts import render

# Create your views here.
def index(request):
    name = "sila Mulingi"
    context = {
        "name": name,
        "phone number": 123456676,
        "age": 45
    }
    return render(request, "index.html", context)
