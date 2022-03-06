from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def homepage(request):
    # return HttpResponse('hello, this is homepage')
    return render(request, 'home.html')
def contact(request):
    return render(request,"contact.html")
def list_books(request):
    books = book.objects.all()
    return render(request,"list_books.html", context={'books':books})
def add_author(request):
    if request.method == "GET":
        addauthor = AddAuthorForm()
        return render(request,'add_author.html', context={'forms': addauthor})
    elif request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        adauthor = author.objects.create(name = name, age = age)
        return HttpResponse("author saved in database")

def add_books(request):
    if request.method =="GET":
        book_form = BookModelForm()
        return render(request,'add_book.html', context={'book_form':book_form})
    else:
        book_form = BookModelForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('list_books')
    return render(request,'add_book.html', context={'book_form':book_form})

def edit_books(request,id):
    books = book.objects.get(id=id)
    if request.method =="GET":
        editbook = BookModelForm(instance=books)
        return render(request,'edit_books.html',{'editbook':editbook})
    else:
        editbook = BookModelForm(request.POST, instance=books)
        if editbook.is_valid():
            editbook.save()
            return redirect('list_books')
    return render(request,'edit_books.html', {'editbook':editbook})

def delete_books(request,id):
    books= book.objects.get(id=id)
    books.delete()
    return redirect("list_books")

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"the email id already exists")
                return redirect("register")
            else:
                user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                user.save()
                print('user created')
                return redirect('register')
        else:
            messages.info(request,'password doesnot match')
            return redirect('register')
        
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
    
        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            messages.info(request,'register if not, or enter correct username and password')
            return redirect('login')
    else:
        return render(request,'login.html')
