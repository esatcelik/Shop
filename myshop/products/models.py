from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    features = models.TextField()
    quantity = models.IntegerField()
    
    def __unicode__(self):
        return self.name

class Bows(models.Model):
    name = models.CharField(max_length=100)

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
