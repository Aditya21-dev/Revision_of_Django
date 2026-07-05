from django.shortcuts import render
# from .models import *

# Create your views here.


def explain(req):
    return render (req , "explain.html")

