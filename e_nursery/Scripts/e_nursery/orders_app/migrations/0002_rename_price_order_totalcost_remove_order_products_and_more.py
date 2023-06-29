# Generated by Django 4.2.2 on 2023-06-28 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0004_delete_users'),
        ('products_app', '0001_initial'),
        ('orders_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='totalCost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.FloatField(default=1)),
                ('customer', models.OneToOneField(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='customer_app.customer')),
                ('products', models.ManyToManyField(related_name='product_order', to='products_app.product')),
            ],
        ),
    ]
