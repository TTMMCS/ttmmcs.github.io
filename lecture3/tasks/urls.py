from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = "apptasks"
urlpatterns = [
    path("", views.index, name = "index"),
    path("add", views.add, name = "adds")
] 

