
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Admin(AbstractUser):

    id=models.AutoField(primary_key=True,auto_created=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    status=models.CharField(max_length=255)

    # Exclude unwanted fields from the model
    is_superuser = None
    is_staff = None
    is_active = None
    date_joined = None
    last_login=None

    # for the database table
    class Meta:
        db_table = "admin"
        managed=False

    # Set the username field to None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

# Add unique related_name for the conflicting fields
Admin.groups.field.remote_field.related_name = 'admin_related_groups'
Admin.user_permissions.field.remote_field.related_name = 'admin_related_user_permissions'

