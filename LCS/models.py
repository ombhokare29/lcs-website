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



# models.py

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/')
    
    def __str__(self):
        return self.name


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    address_city = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255)
    address_postal_code = models.CharField(max_length=20)
    address_country = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Donation by {self.name} of {self.amount}'


