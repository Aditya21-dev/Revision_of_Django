from django.shortcuts import render , redirect
from .models import Student

# Create your views here.


def get(request):
    if request.method == "POST":

        Student.objects.create(

            name=request.POST.get("name"),
            age=request.POST.get("age"),
            email=request.POST.get("email"),
            course=request.POST.get("course"),
            city=request.POST.get("city"),

        )

        return redirect("show")
     
    return render(request, "get.html")

   


def show(request):

    students = Student.objects.all()

    context = {
        "students": students
    }

    return render(request, "show.html", context)