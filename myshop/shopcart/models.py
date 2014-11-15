from django.db import models
# Create your models here.

class Cart(models.Model):
    user_id=models.CharField(max_length=100)
    bow_id=models.CharField(max_length=200)
    arrow_id=models.CharField(max_length=200)
    accessory_id=models.CharField(max_length=200)

    def __unicode__(self):
        return self.name