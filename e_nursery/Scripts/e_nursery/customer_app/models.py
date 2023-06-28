from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    # Exclude unwanted fields from the model
    is_superuser = None
    is_staff = None
    is_active = None
    date_joined = None
    last_login=None

    class Meta:
        db_table = "customer"

    # Set the username field to None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

#Model for Users
class Users(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=255)

    # for the database table
    class Meta:
        managed = False  # Set managed=False to indicate that this model is not managed by Django
        db_table = 'users'  # Set the name of the database view
