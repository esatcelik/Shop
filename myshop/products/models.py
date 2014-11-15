from django.db import models

# Create your models here.
class Bows(models.Model):
    BOW_TYPES = (
        ('C', 'Compounds'),
        ('R', 'Recurves'),
        ('T', 'Traditional'),
    )
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=BOW_TYPES)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Arrows(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Accessories(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
