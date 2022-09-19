from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Books
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.



def index(request):
    books = Books.objects.all().values("issued_from__name","issued_from__id","issued_from__location","book_name","book_author","issued_from__id","image")
    
    return render (request,"index.html",{"books":books})

def search(request):
    return render(request,"search.html")

def search_action(request):
    search_item = request.GET.get("search_item")
    books = list(Books.objects.filter(issued_from__name__icontains=search_item).values("book_name","book_author","issued_from__name","issued_from__id","issued_from__location"))
    return JsonResponse({"filtered_results":books})

def signup(request):
    return render(request,"signup.html")

def signup_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    user = User.objects.create_user(username=username,password=password,first_name=name)
    auth.login(request,user=user)
    return redirect('index')

def signin(request):
    return render(request,"signin.html")

def signin_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    print(username,password)
    user = auth.authenticate(request,username=username,password=password)
    auth.login(request,user)
    return redirect('index')

def Payel(request):
    return HttpResponse('<h1>Hii</h1>')