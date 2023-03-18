from django.contrib import admin
from .models import Book, Writer


class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_at', 'died_at', 'books', 'contact', 'bio')
    
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'published_at', 'summary', 'writer', 'country', 'link')


# register the Writer model with the WriterAdmin class
admin.site.register(Writer, WriterAdmin)
admin.site.register(Book, BookAdmin)
