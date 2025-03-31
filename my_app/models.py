from django.db import models

# Create your models here.

class signup(models.Model):
    first_name=models.CharField(max_length=200, null=True, blank=True, default="")
    last_name=models.CharField(max_length=200, null=True, blank=True, default="")
    Password=models.CharField(max_length=250, null=True, blank=True, default="")
    Mobile=models.BigIntegerField(default='', null=True)
    Email = models.EmailField(null=True)
    
    def __str__(self):
        return self.first_name