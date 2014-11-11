from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    features = models.TextField()
    quantity = models.IntegerField()
    
    def __unicode__(self):
        return self.name

class Gpu(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name