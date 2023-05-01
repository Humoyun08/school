from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mentor(models.Model):
    full_name = models.CharField(max_length=(155))
    fani = models.CharField(max_length=(155))
    malumoti = models.CharField(max_length=(155))
    sinfi = models.CharField(max_length=(155))
    
    def __str__(self):
        return self.full_name
    
class A1_class(models.Model):
    full_name = models.CharField(max_length=(155))
    birth_data = models.DateField()
    age = models.IntegerField()
    sinfi = models.IntegerField()
    qabul_qilingan_kun = models.DateField()
    
    def __str__(self):
        return self.full_name
    


    
    
 