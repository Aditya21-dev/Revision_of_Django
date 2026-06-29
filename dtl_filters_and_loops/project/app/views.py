from django.shortcuts import render

# Create your views here.

def home(req):
    name = "Aditya"
    age = 19
    email = "adityadas0217@gmail.com"
    marks = {
        "python" : 47,
        "django" : 50,
        "c++" : 42,
        "java" : 50
    }

    context = {
        "name" : name,
        "age" : age,
        "email" : email,
        "marks" : marks,
    }

    return render(req , "home.html" , context)