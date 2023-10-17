
from django.shortcuts import render, redirect
from .models import Student, Education

def index(request):
    return render(request, 'registration.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        university = request.POST['university']
        year = request.POST['year']

        student = Student.objects.create(name=name, email=email)


        Education.objects.create(student=student, course=course, university=university, year=year)

        return redirect('registration.html')

    return redirect('registration.html')
