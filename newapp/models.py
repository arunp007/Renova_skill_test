from django.db import models

class Registration(models.Model):
    fullname = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    cpassword = models.TextField(max_length=100)
    auth = models.TextField(max_length=50)

class Meta:
    db_table = 'registration'
