from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class volunteer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    availability = models.CharField(max_length=50)

class sponsorship(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    availability = models.CharField(max_length=50)
    


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    query = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"
    

class create_checkout_session(models.Model):
    amount = models.CharField(max_length=100)




