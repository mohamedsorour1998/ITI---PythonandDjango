from django.contrib import admin
from .models import Writer


class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_at', 'died_at', 'books', 'contact', 'bio')


# register the Writer model with the WriterAdmin class
admin.site.register(Writer, WriterAdmin)
