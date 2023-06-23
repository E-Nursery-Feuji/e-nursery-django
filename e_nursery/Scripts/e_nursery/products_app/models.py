from django.db import models

class Image(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True,default=2)
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
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField()
    image = models.OneToOneField(Image, on_delete=models.SET_DEFAULT, default=1)
    type_id = models.ForeignKey(Type, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        db_table = "product"



# class Cart(models.Model):
#     id=models.AutoField(primary_key=True)  
#     quantity=models.IntegerField()
#     customer_id=models.ForeignKey()   