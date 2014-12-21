from django.db import models

class Review(models.Model):
    
    pro_id = models.IntegerField()
    name = models.TextField()
    review = models.TextField()
    date = models.TextField()
    
    
    def __unicode__(self):
        return self.pro_id