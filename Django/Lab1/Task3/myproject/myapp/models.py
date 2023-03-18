from django.db import models
from django.urls import reverse


# Create your models here.
class Writer(models.Model):
    name = models.CharField(max_length=100)
    born_at = models.DateField()
    died_at = models.DateField(null=True, blank=True)
    books = models.TextField()
    contact = models.TextField()
    bio = models.TextField()
    
    def __str__(self):
        return self.name




class Book(models.Model):
    name = models.CharField(max_length=200)
    published_at = models.DateField()
    summary = models.TextField()
    writer = models.ForeignKey('Writer', on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])
