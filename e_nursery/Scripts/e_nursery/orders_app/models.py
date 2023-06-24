from django.db import models

# Create your models here.
class Delivery_status(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=300)
    class Meta:
        db_table = 'delivery_status'


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    mode = models.CharField(max_length=300)
    payment_status = models.CharField(max_length=300)
    transaction_id = models.CharField(max_length=300)
    class Meta:
        db_table = 'payment'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
