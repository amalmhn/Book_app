from django.shortcuts import render, redirect
from .forms import *
from .models import Book
# Create your views here.

#1)book/create
'''get=> get functionality for creating book, return all book objects
    post=>creating a book'''
def book_create(request):
    #get
    form = BookCreateForm()
    context = {}
    context['form'] = form
    books = Book.objects.all()
    context['book'] = books
    if request.method == 'POST':
        form  = BookCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            context['form'] = form
            return render(request,'bookapp/bookCreate.html',context)
    return render(request,'bookapp/bookCreate.html',context)
    #post



#2)book/view/1
'''get=> return book with corresponding id'''
def view_book(request,id):
    book = Book.objects.get(id=id)
    context = {}
    context['book'] = book
    return render(request,'bookapp/bookView.html',context)


#3)book/update/1
'''get=> return book with correspoding id
    post=>update book'''
def update_book(request,id):
    book = Book.objects.get(id=id)
    form = BookUpdateForm(instance=book)
    context = {}
    context['book'] = book
    context['form'] = form
    if request.method=='POST':
        form = BookUpdateForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            form = BookUpdateForm(request.POST,request.FILES, instance=book)
            context = {}
            context['form'] = form
            return render(request, 'bookapp/bookEdit.html', context)
    return render(request,'bookapp/bookEdit.html',context)

#4)book/delete/1
'''get=>delete book with id'''
def delete_book(request,id):
    book = Book.objects.get(id=id).delete()
    return redirect('create')

#homepage
'''get>html page with home'''
def home(request):
    book = Book.objects.all()
    context = {}
    context['book'] = book
    return render(request,'bookapp/index.html',context)