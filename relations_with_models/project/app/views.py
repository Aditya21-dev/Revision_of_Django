from django.shortcuts import render
from .models import Student , Class , Teacher , Subject , IDCard

# Create your views here.

from django.shortcuts import render


def home(request):
    return render(request, "home.html")



def add_student(request):

    classes = Class.objects.all()
    subjects = Subject.objects.all()

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        class_id = request.POST.get("classroom")
        subject_ids = request.POST.getlist("subjects")

        classroom = Class.objects.get(id=class_id)

        student = Student.objects.create(
            name=name,
            age=age,
            Class_room=classroom
        )

        for id in subject_ids:
            subject = Subject.objects.get(id=id)
            student.subjects.add(subject)

    context = {
        "page": "student",
        "classes": classes,
        "subjects": subjects,
    }

    return render(request, "home.html", context)




def add_teacher(request):

    if request.method == "POST":

        Teacher.objects.create(
            name=request.POST.get("name"),
            salary=request.POST.get("salary")
        )

    return render(request, "home.html", {"page": "teacher"})



def add_subject(request):

    teachers = Teacher.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        teacher_id = request.POST.get("teacher")
        teacher = Teacher.objects.get(id=teacher_id)

        Subject.objects.create(
            subject_name=subject_name,
            teacher=teacher
        )

    context = {
        "page": "subject",
        "teachers": teachers
    }

    return render(request, "home.html", context)



def add_class(request):

    if request.method == "POST":

        Class.objects.create(
            class_name=request.POST.get("class_name"),
            room_no=request.POST.get("room_no")
        )

    return render(request, "home.html", {"page": "class"})



def add_idcard(request):
    students = Student.objects.all()

    if request.method == "POST":
        card_number = request.POST.get("card_number")
        issue_date = request.POST.get("issue_date")
        student_id = request.POST.get("student")
        student =  Student.objects.get(id=student_id)

        IDCard.objects.create(
            card_number = card_number,
            issue_date = issue_date,
            student = student
        )
    return render(request, "home.html", {"page": "idcard" , "students":students})







def show(request):

    students = Student.objects.all()

    return render(request, "show.html", {"students": students})






