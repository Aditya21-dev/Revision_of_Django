from django.shortcuts import render
from .models import Student , Class , Teacher , Subject , IDCard

# Create your views here.

from django.shortcuts import render


def home(request):
    return render(request, "home.html")












def add_student(request):
    return render(request, "home.html", {"page": "student"})













def add_teacher(request):

    if request.method == "POST":

        Teacher.objects.create(
            name=request.POST.get("name"),
            salary=request.POST.get("salary")
        )

    return render(request, "home.html", {"page": "teacher"})











def add_subject(request):
    teacher = Teacher.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get("subject_name") 
        teacher_id = request.POST.get("teacher") 
        teacher = Teacher.objects.get(id = teacher_id) 

        Subject.objects.create(
            subject_name = subject_name,
            teacher = teacher
        )
        
    return render(request , "home.html" , 
                  "page":"subject" , 
                  "teachers":teacher)










def add_class(request):

    if request.method == "POST":

        Class.objects.create(
            class_name=request.POST.get("class_name"),
            room_no=request.POST.get("room_no")
        )

    return render(request, "home.html", {"page": "class"})

















def add_idcard(request):
    return render(request, "home.html", {"page": "idcard"})