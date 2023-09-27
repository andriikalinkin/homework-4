from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("generate-student/", views.students, name="generate-student"),
    path("generate-students/", views.generate_students, name="generate-students"),
]