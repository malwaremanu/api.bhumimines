from django.db import models
from django.utils import timezone
import datetime, uuid

# Create your models here.
class cashbook(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.TextField()
    username = models.TextField()
    mobile_no = models.TextField(blank=True)
    photo = models.TextField(default='sample.jpeg', blank=True)
    email = models.TextField(blank=True)
    password = models.TextField()

    def __str__(self):
        return str(self.username + "####" + self.password)    

    def up(self):
        return str(self.username + "####" + self.password)    

    def userpass(self):        
        return {
            "uuid" : str(self.uuid),
            "name" : self.name,
            "photo" : self.photo,
            "username" : self.username,            
            "password" : self.password,
            "email" : self.email,
            "mobile_no" : self.mobile_no,
        }        