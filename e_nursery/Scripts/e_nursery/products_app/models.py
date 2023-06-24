from django.db import models

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=300)
    class Meta:
        db_table = 'image'

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=40)

    class Meta:
        db_table = "type"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    discount = models.FloatField()
    quantity = models.FloatField()
    image = models.OneToOneField(Image, on_delete=models.CASCADE) 
    type = models.ForeignKey(Type, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        db_table = "product"



  