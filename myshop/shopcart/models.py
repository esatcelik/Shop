from django.db import models
# Create your models here.

class Cart(models.Model):
    user_id1=models.CharField(max_length=100)
    bow_id1=models.CharField(max_length=200,blank=True)
    arrow_id1=models.CharField(max_length=200,blank=True)
    accessory_id1=models.CharField(max_length=200,blank=True)

    def __unicode__(self):
        return self.user_id1