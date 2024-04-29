from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Course

def home(request):
    return render(request, 'course/home.html')

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def user_login(request):
    # Handle login logic here
    return render(request, 'course/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
