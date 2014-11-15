from django.db import models

# Create your models here.
class Bows(models.Model):
    BOW_TYPES = (
        ('Compounds', 'Compounds'),
        ('Recurves', 'Recurves'),
        ('Traditional', 'Traditional'),
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
    ARR_TYPES = (
        ('Aluminium', 'Aluminium'),
        ('Carbon', 'Carbon'),
        ('Wood', 'Wood'),
    )
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=ARR_TYPES)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Accessories(models.Model):
    ACS_TYPES = (
        ('Bow', 'Bow'),
        ('Arrow', 'Arrow'),
        ('General', 'General'),
    )
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=ACS_TYPES)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __unicode__(self):
        return self.name
