from django.db import models

# created by Priya Patel & Samundar Singh Rathore
# Create your models here.

# Model for Customer
class Customer(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    
    # for the database table
    class Meta:
        db_table = "customer"
        managed=False

#Model for Users
class Users(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=255)

#     # for the database table
    class Meta:
        managed = False  # Set managed=False to indicate that this model is not managed by Django
        db_table = 'users'  # Set the name of the database view
