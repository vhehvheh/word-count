from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'world.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def day(request):
    return render(request, 'day.html')