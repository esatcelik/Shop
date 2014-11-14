from django.db import models

# Create your models here.
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
