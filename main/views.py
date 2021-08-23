from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import ToDoList,Item

def index(response,id):
    ls=ToDoList.objects.get(id=id)
    return render(response,"./list.html",{"ls":ls})

def home(response):
    return render(response,"./home.html",{})