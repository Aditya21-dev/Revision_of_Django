from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render
from .models import Student

def form(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        city = request.POST.get("city")
        course = request.POST.get("course")
        marks = request.POST.get("marks")
        gender = request.POST.get("gender")
        admission_date = request.POST.get("admission_date")
        is_active = True if request.POST.get("is_active") else False

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            city=city,
            course=course,
            marks=marks,
            gender=gender,
            admission_date=admission_date,
            is_active=is_active
        )

        return render(request, "form.html", {"msg": "Student Saved Successfully"})

    return render(request, "form.html")





# 1. all()
def all_data(request):
    data = Student.objects.all().values()
    return HttpResponse(f"<pre>{list(data)}</pre>")


# 2. filter()
def filter_data(request):
    data = Student.objects.filter(city="Bhopal").values()
    return HttpResponse(f"<pre>{list(data)}</pre>")


# 3. exclude()
def exclude_data(request):
    data = Student.objects.exclude(city="Bhopal").values()
    return HttpResponse(f"<pre>{list(data)}</pre>")


# 4. order_by()
def order_data(request):
    data = Student.objects.order_by("marks").values()
    return HttpResponse(f"<pre>{list(data)}</pre>")


# 5. values()
def values_data(request):
    data = Student.objects.values("name", "marks", "city")
    return HttpResponse(f"<pre>{list(data)}</pre>")


# 6. values_list()
def values_list_data(request):
    data = Student.objects.values_list("name", flat=True)
    return HttpResponse(f"<pre>{list(data)}</pre>")


# 7. get()
def get_data(request):
    try:
        data = Student.objects.get(id=1)
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(str(e))


# 8. first()
def first_data(request):
    data = Student.objects.first()
    return HttpResponse(str(data))


# 9. last()
def last_data(request):
    data = Student.objects.last()
    return HttpResponse(str(data))


# 10. latest()
def latest_data(request):
    try:
        data = Student.objects.latest("created_at")
        return HttpResponse(str(data))
    except Exception as e:
        return HttpResponse(str(e))


# 11. earliest()
def earliest_data(request):
    try:
        data = Student.objects.earliest("created_at")
        return HttpResponse(str(data))
    except Exception as e:
        return HttpResponse(str(e))


# 12. count()
def count_data(request):
    data = Student.objects.count()
    return HttpResponse(str(data))


# 13. exists()
def exists_data(request):
    data = Student.objects.filter(city="Bhopal").exists()
    return HttpResponse(str(data))


# 14. update()
def update_data(request):
    Student.objects.filter(id=2).update(marks=100)
    return HttpResponse("Updated Successfully")


# 15. delete()
def delete_data(request):
    Student.objects.filter(id=1).delete()
    return HttpResponse("Deleted Successfully")


# 16. get_or_create()
def get_or_create_data(request):
    student, created = Student.objects.get_or_create(
        email="mahakoi@gmail.com",
        defaults={
            "name": "mahak",
            "age": 20,
            "city": "Bhopal",
            "course": "B.Com",
            "marks": 90,
            "gender": "Female",
            "admission_date": "2006-03-13",
        }
    )
    return HttpResponse(str(created))


# 17. update_or_create()
def update_or_create_data(request):
    student, created = Student.objects.update_or_create(
        email="mahakoi@gmail.com",
        defaults={
            "marks": 89,
        }
    )
    return HttpResponse(str(created))


# 18. bulk_create()
def bulk_create_data(request):
    students = [
        Student(
            name="Rahul",
            age=20,
            email="rahul157@gmail.com",
            city="Bhopal",
            course="Python",
            marks=80,
            gender="Male",
            admission_date="2006-07-01",
        ),
        Student(
            name="Man",
            age=21,
            email="Man14@gmail.com",
            city="Indore",
            course="Django",
            marks=85,
            gender="Male",
            admission_date="2006-07-01",
        ),
    ]

    Student.objects.bulk_create(students)
    return HttpResponse("Bulk Insert Successful")