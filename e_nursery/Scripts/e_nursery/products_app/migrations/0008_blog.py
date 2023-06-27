# Generated by Django 4.2.1 on 2023-06-24 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0007_alter_image_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('uploaded_by', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=40)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.image')),
            ],
        ),
    ]