from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Library,Books

# Create your views here.



def index(request):
    books = Books.objects.all().values("issued_from__name","issued_from__id","issued_from__location","book_name","book_author","issued_from__id")
    print(books)
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
    username = request.BOOKS.get("email")
    password = request.BOOKS.get("password")
    name = request.BOOKS.get("name")
    user = User.objects.create_user(username=username,password=password,first_name=name)
    auth.login(request,user=user)
    return redirect('index')


def Payel(request):
    return HttpResponse('<h1>Hii</h1>')