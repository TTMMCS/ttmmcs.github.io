from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("tung", views.tung, name="tung"),
    path("hanh", views.hanh, name="hanh"),
    path("<ame>", views.greet)
]