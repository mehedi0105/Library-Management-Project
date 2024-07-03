from django.shortcuts import render


from django.shortcuts import render
from books.models import Book
from category.models import Category
def homepage(request, category_slug = None):
    
    data = Book.objects.all() 
    if category_slug is not None: 
        category = Category.objects.get(slug = category_slug) 
        data = Book.objects.filter(category  = category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data' : data, 'category' : categories})
    