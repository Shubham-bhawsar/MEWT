from django.db import models

# Create your models here.
class Formdata(models.Model):
    passw=models.CharField(max_length=244)
    email=models.EmailField()