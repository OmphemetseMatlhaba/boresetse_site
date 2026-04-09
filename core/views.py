# core/views.py

from django.shortcuts import render, redirect
from .models import *

# core/views.py

def home(request):
    return render(request, "home.html", {
        "school": School.objects.first(),
        "hero": Hero.objects.first(),
        "posts": Post.objects.all()[:3],
        "principal": PrincipalMessage.objects.first(),
    })


def about(request):
    return render(request, "about.html", {
        "about": About.objects.first(),
        "code_of_conduct": CodeOfConduct.objects.first()
    })


def gallery(request):
    return render(request, "gallery.html", {
        "images": GalleryImage.objects.all()
    })


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            message=request.POST["message"]
        )
        return redirect("/contact")

    return render(request, "contact.html")

def principal_message(request):
    return render(request, "principal_message.html", {
        "principal": PrincipalMessage.objects.first()
    })
def payments(request):
    return render(request, "payments.html")


def mural_activities(request):
    return render(request, "mural_activities.html", {
        "activities": MuralActivity.objects.all()
    })


def top_students(request):
    # Get top students grouped by grade, ordered from 12 to 8
    grades = [12, 11, 10, 9, 8]
    students_by_grade = {}
    for grade in grades:
        students_by_grade[grade] = TopStudent.objects.filter(grade=grade).order_by('position')[:10]
    
    return render(request, "top_students.html", {
        "students_by_grade": students_by_grade
    })


def staff_sgb(request):
    return render(request, "staff_sgb.html", {
        "staff": StaffMember.objects.all(),
        "sgb": SGBMember.objects.all()
    })


def newsletter(request):
    return render(request, "newsletter.html", {
        "newsletters": Newsletter.objects.all()
    })