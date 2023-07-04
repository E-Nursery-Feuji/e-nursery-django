from django.db import models

def upload_path(instance,filename):
    return '/'.join(['images',str(instance.id),filename])

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(blank=False,null=True,upload_to=upload_path)
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
    image_id = models.OneToOneField(Image, on_delete=models.CASCADE) 
    type_id = models.ForeignKey(Type, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        db_table = "product"


class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)
    uploaded_by=models.CharField(max_length=50)
    status=models.CharField(max_length=40)
    class Meta:
        db_table="blog"
