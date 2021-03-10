from django.shortcuts import render, redirect

# Create your views here.
#In class based view django have some in built funtions like below:
#DetailView , UpdateView , DeleteView , ListVIew , CreateVIew(all these views are predefined)

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# class BookList(ListView):
#     model = Book
#     # context_object_name =
#     # template_name =

class BookList(ListView):
    model = Book
    context = {}
    template_name = 'cbvbook/book_list.html'
    #get
    def get(self, request, *args, **kwargs):
        books = self.model.objects.all()
        self.context['books'] = books
        return render(request,self.template_name,self.context)

# class BookView(DetailView):
#     model = Book
#     template_name = 'cbvbook/bookDetail.html'
#     context_object_name = 'book'

class BookView(TemplateView):
    model = Book
    template_name = 'cbvbook/bookDetail.html'
    context = {}
    def get(self, request, *args, **kwargs):
        #print(kwargs)  {pk:1}
        id = kwargs.get('pk')
        book = self.model.objects.get(id=id)
        self.context['book'] = book
        return render(request,self.template_name,self.context)

# class BookCreate(CreateView):
#     model = Book
#     form_class = BookCreateForm
#     template_name = 'cbvbook/bookCreate.html'
#     success_url = reverse_lazy('list')

class BookCreate(TemplateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'cbvbook/bookCreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return render(request,self.template_name,self.form)

class BookUpdate(TemplateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'cbvbook/bookCreate.html'
    context = {}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        # book = self.model.objects.get(id=id)
        book = self.get_object(id)
        form = self.form_class(instance=book)
        self.context['form'] = form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        book = self.get_object(id)
        form = self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return render(request,self.template_name,self.context)

class BookDelete(TemplateView):
    model = Book
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        book = self.get_object(id)
        book.delete()
        return redirect('list')


