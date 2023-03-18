from .models import Writer, Book
from django.shortcuts import render

# Create your views here.
def home(request):
    writers = Writer.objects.all()
    context = {'writers': writers}
    return render(request, 'myapp/home.html', context)


def writer_detail(request,writer_id):
    writer = Writer.objects.get(id=writer_id)
    context = {'writer': writer}
    return render(request, 'myapp/writer_detail.html', context)

def BookDetailView(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'myapp/book_detail.html', context)