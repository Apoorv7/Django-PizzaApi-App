from django.db import models

# Create your models here.
class Pizza(models.Model):
    Ptype = models.CharField(max_length=100)
    Psize = models.CharField(max_length=100)
    Ptop = models.CharField(max_length=100)
