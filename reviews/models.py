from django.db import models

class Reviews(models.Model):
    
    pro_id = models.IntegerField()
    review = models.TextField()
    username = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    mod = models.TextField()
    
    
    def __unicode__(self):
        return unicode(self.pro_id) or u''  # @UndefinedVariable
