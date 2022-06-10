from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method =="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        comments =request.POST.get('comments')
        contact = Contact(name=name, email=email, phone= phone, comments=comments, date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def pizza(request):
    return render(request,'pizza.html')

def burger(request):
    return render(request,'burger.html')

def colddrinks(request):
    return render(request,'colddrinks.html')