from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from faker import Faker

from . import models


fake = Faker()


def index(request):
    return HttpResponse("<h1>Homework-4 index page</h1>")


def students(request):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=30)

    student = models.Student(first_name=first_name, last_name=last_name, birth_date=birth_date)
    student.save()

    return render(request, "generate_student.html", {"student": student})


def generate_students(request):
    try:
        count = int(request.GET.get("count", 10))

        if count <= 0 or count > 100:
            return HttpResponse("The `count` parameter must be from 1 to 100.\n"
                                "For example, you can enter `.../generate-students/?count=10` in the address bar.")

        students_list = []

        for i in range(count):
            first_name = fake.first_name()
            last_name = fake.last_name()
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=30)

            student = models.Student(first_name=first_name, last_name=last_name, birth_date=birth_date)
            student.save()

            students_list.append(student)

        return render(request, "generate-students.html", {"students_list":students_list})

    except ValueError:
        return HttpResponseBadRequest("To generate and save couple students try `.../generate-students/?count=10`.")
