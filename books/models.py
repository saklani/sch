from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)

class Book(models.Model):
    title  = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags   = models.ManyToManyField('Tag', blank=True)
    published_year = models.IntegerField(default=2024)
    is_out_of_print = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=32)


