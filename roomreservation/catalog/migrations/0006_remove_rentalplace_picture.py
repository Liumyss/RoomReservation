# Generated by Django 4.1.7 on 2023-02-17 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rentalplace_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentalplace',
            name='picture',
        ),
    ]
