from django.db import models
from django.utils import timezone
import datetime, uuid

# Create your models here.
class cashbook(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
        
    opening_balance = models.TextField(blank=True)
    closing_balance = models.TextField(blank=True)
    
    user = models.CharField(max_length=50)
    
    date = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.user + ' - ' + self.date)    

    def json_data(self):        
        return {
            "uuid" : str(self.uuid),
            "opening_balance" : self.opening_balance,
            "closing_balance" : self.closing_balance,
            "date" : self.date,            
            "user" : self.user,
        }        