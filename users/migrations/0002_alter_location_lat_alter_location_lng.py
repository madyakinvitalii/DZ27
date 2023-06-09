# Generated by Django 4.2.1 on 2023-06-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
    ]
