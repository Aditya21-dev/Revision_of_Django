from django.shortcuts import render

# Create your views here.

def form(request):
    if request.method == "POST":

        context = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "age": request.POST.get("age"),
            "phone": request.POST.get("phone"),
            "website": request.POST.get("website"),
            "search": request.POST.get("search"),
            "date": request.POST.get("date"),
            "time": request.POST.get("time"),
            "datetime": request.POST.get("datetime"),
            "month": request.POST.get("month"),
            "week": request.POST.get("week"),
            "color": request.POST.get("color"),
            "experience": request.POST.get("experience"),
            "gender": request.POST.get("gender"),
            "city": request.POST.get("city"),
            "address": request.POST.get("address"),
            
            "python": request.POST.get("python"),
            "java": request.POST.get("java"),
            "django": request.POST.get("django"),
        }

        return render(request, "show.html", context)

    return render(request, "form.html")


def show(req):
    return render(req , "show.html")