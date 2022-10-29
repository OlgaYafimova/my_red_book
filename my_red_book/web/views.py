from django.shortcuts import render
from .models import Red_book

def Red_bookView(request):
    context = {
        'key_red_book_values': Red_book.objects.all()
    }
    return render(request, 'red_book/red_book.html', context)

def Red_book_detailView(request,num):
    context = {
        'key_red_book_1item': Red_book.objects.filter(id=num)
    }
    return render(request, 'red_book/red_book_detail.html', context)