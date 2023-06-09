# Generated by Django 4.2.1 on 2023-06-09 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='is_published',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
