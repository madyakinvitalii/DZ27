# Generated by Django 4.2.1 on 2023-06-09 09:51

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_age_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, validators=[users.models.validate_email_domain]),
        ),
    ]
