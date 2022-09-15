from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)

    def _str_(self):
        return self.name

class Books(models.Model):
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    issued_from = models.ForeignKey(Library,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name


