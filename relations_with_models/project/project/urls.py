"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name="home"),
    path('add_student/' , views.add_student , name="add_student"),
    path('add_class/' , views.add_class , name="add_class"),
    path('add_teacher/' , views.add_teacher, name="add_teacher"),
    path('add_subject/' , views.add_subject , name="add_subject"),
    path('add_idcard/' , views.add_idcard , name="add_idcard"),
    path('show/' , views.show , name="show"),
]
