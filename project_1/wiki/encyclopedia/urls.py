from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title_1"),
    path("random", views.random, name="random_title"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("save", views.save, name="save"),
]
