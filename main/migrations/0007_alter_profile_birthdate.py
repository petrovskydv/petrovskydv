# Generated by Django 3.2.3 on 2021-06-11 07:54

from django.db import migrations, models
import main.models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True, validators=[main.utils.validate_birthday], verbose_name='дата рождения'),
        ),
    ]
