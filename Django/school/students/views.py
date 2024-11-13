from django.shortcuts import render
from django.shortcuts import redirect
from students.models import Student
# Create your views here.
def home(request):
    return render(request, 'home.html')


def insert(request):
    return render(request, 'insert.html')

def insertData(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']

        student = Student(name=name, email=email, phone=phone, age=age)
        student.save()
        return redirect('/')
    return render(request, 'insert.html')

def viewtable(request):
    students = Student.objects.all()
    return render(request, 'viewdata.html', {'students': students})