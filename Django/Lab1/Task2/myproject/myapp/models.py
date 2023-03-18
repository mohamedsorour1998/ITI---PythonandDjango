from django.db import models

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
    
