# Generated by Django 3.2.3 on 2021-06-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_profile_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images'),
        ),
    ]