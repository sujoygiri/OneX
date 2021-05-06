from django.db import models
from django.db.models import BigAutoField
# Create your models here.
class EncrypteMessage(models.Model):
    
    en_message = models.TextField(default="")
    en_shift_value = models.IntegerField(default="")

    def __str__(self):
        return self.en_message
    
class DecrypteMessage(models.Model):
    
    de_message = models.TextField(default="")
    de_shift_value = models.IntegerField(default="")

    def __str__(self):
        return self.de_message