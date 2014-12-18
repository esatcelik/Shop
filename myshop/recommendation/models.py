from django.db import models

class Rec(models.Model):
    
    user1_id = models.IntegerField()
    rec_bow = models.TextField()
    rec_arrow = models.TextField()
    rec_accessory = models.TextField()
    
    def __unicode__(self):
        return unicode(self.user1_id) or u''  # @UndefinedVariable