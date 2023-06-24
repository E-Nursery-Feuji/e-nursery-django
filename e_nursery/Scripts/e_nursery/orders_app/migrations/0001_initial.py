# Generated by Django 4.1.9 on 2023-06-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'delivery_status',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mode', models.CharField(max_length=300)),
                ('payment_status', models.CharField(max_length=300)),
                ('transaction_id', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
