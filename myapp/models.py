from django.db import models

# Create your models here.
class Formdata(models.Model):
    passw=models.CharField(max_length=244)
    email=models.EmailField()

class Contacts(models.Model):
    Email = models.CharField(max_length=244)
    Name = models.CharField(max_length=244)
    Message = models.CharField(max_length=244)
    Subject = models.CharField(max_length=244)
    def __str__(self):
        return self.Name
    
