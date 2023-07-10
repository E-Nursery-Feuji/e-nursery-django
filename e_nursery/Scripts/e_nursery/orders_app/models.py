from django.db import models
from customer_app.models import Customer
from products_app.models import Product
import datetime




class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.FloatField(default=1)
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "cart"



