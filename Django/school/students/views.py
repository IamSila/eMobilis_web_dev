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
        # image = request.FILES['image']

        student = Student(name=name, email=email, phone=phone, age=age)
        student.save()
        return redirect('/')
    return render(request, 'insert.html')

def viewtable(request):
    students = Student.objects.all()
    return render(request, 'viewdata.html', {'students': students})

def edit(request, id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        # image = request.FILES['image']


        student = Student.objects.get(id=id)

        student.name = name
        student.email = email
        student.phone = phone
        student.age = age
        
        student.save()

    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {"student": student})