
from django.db import models

# Create your models here.
class Admin(models.Model):

    id=models.AutoField(primary_key=True,auto_created=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    
    # for the database table
    class Meta:
        db_table = "admin"
        managed=False