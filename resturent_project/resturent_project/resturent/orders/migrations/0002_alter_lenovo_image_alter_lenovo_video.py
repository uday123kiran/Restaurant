# Generated by Django 5.0.4 on 2024-04-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lenovo',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='lenovo',
            name='video',
            field=models.FileField(upload_to=''),
        ),
    ]