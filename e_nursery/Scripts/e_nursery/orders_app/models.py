# from django.db import models
# from customer_app.models import Customer
# from products_app.models import Product
# import datetime

# class DeliveryStatus(models.Model):
#     id = models.AutoField(primary_key=True)
#     status = models.CharField(max_length=300)

#     class Meta:
#         db_table = 'delivery_status'
       


# class Payment(models.Model):
#     id = models.AutoField(primary_key=True)
#     mode = models.CharField(max_length=300)
#     payment_status = models.CharField(max_length=300)
#     transaction = models.CharField(max_length=300)

#     class Meta:
#         db_table = 'payment'


# class Cart(models.Model):
#     id = models.AutoField(primary_key=True)
#     quantity = models.FloatField(default=1)
#     customer = models.OneToOneField(
#         Customer, on_delete=models.SET_DEFAULT, default=1)
#     products = models.ManyToManyField(Product,related_name="product_order",)


# class Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     quantity = models.FloatField(default=1)
#     totalCost = models.FloatField(default=0.0)
#     order_date = models.DateField(default=datetime.date.today)
#     payment = models.OneToOneField(Payment, on_delete=models.CASCADE,default=1)
#     delivery= models.ForeignKey(
#         DeliveryStatus, on_delete=models.SET_DEFAULT, default=1)
#     products = models.ForeignKey(Product,on_delete=models.SET_DEFAULT,default=1)
#     customer = models.ForeignKey(
#         Customer, on_delete=models.SET_DEFAULT, default=1)
    

#     class Meta:
#         db_table = 'order'
