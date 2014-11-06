from shop.models import Product
from django.db import models

class Book(Product):
    # The author should probably be a foreign key in the real world, but
    # this is just an example
    author = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to='img/book')
    isbn = models.CharField(max_length=255)

    class Meta:
        ordering = ['author']