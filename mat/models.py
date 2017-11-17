from django.db import models

# Create your models here.

class MatLemma(models.Model):
    material_titel = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
