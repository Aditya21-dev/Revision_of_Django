from django.shortcuts import render , redirect
from .models import User


# Create your views here.

def form(req):

    if req.method == "POST":

        User.objects.create(
            name=req.POST.get("name"),
            email=req.POST.get("email"),
            phone=req.POST.get("phone"),
            address=req.POST.get("address"),
            profile_img=req.FILES.get("image")
        )

        return redirect("home")
    
    return render(req , "form.html")


def home(req):
    users = User.objects.all()
    return render(req , "home.html" , {"users":users})