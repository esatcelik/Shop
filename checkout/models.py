from django.db import models

# Create your models here.

class Check(models.Model):
    user_id1=models.CharField(max_length=100)
    bow_data=models.CharField(max_length=500,blank=True)
    arrow_data=models.CharField(max_length=500,blank=True)
    accessory_data=models.CharField(max_length=500,blank=True)
    Tprice = models.IntegerField()
    used = models.IntegerField()
    
    def __unicode__(self):
        return self.user_id1

class Package(models.Model):
    user_id1=models.CharField(max_length=100)
    quantity = models.IntegerField()
    Tprice = models.IntegerField()
    real_id = models.IntegerField()
    
    def __unicode__(self):
        return self.user_id1