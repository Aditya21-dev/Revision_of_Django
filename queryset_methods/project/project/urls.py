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
    path('' , views.form , name="form"),

    path("all/", views.all_data, name="all_data"),
    path("filter/", views.filter_data, name="filter_data"),
    path("exclude/", views.exclude_data, name="exclude_data"),
    path("order/", views.order_data, name="order_data"),
    path("values/", views.values_data, name="values_data"),
    path("values-list/", views.values_list_data, name="values_list_data"),
    path("get/", views.get_data, name="get_data"),
    path("first/", views.first_data, name="first_data"),
    path("last/", views.last_data, name="last_data"),
    path("latest/", views.latest_data, name="latest_data"),
    path("earliest/", views.earliest_data, name="earliest_data"),
    path("count/", views.count_data, name="count_data"),
    path("exists/", views.exists_data, name="exists_data"),
    path("update/", views.update_data, name="update_data"),
    path("delete/", views.delete_data, name="delete_data"),
    path("get-or-create/", views.get_or_create_data, name="get_or_create_data"),
    path("update-or-create/", views.update_or_create_data, name="update_or_create_data"),
    path("bulk-create/", views.bulk_create_data, name="bulk_create_data"),
]
