from django.db import models
# Create your models here.

class Cart(models.Model):
    user_id1=models.CharField(max_length=100)
    data=models.CharField(max_length=500,blank=True)

    def __unicode__(self):
        return self.user_id1