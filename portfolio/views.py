from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def experience(request):
    return render(request, 'experience.html')


def contact(request):
    
    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )

        messages.success(request, "Your message has been sent successfully!")

        return redirect("contact")

    return render(request, "contact.html")