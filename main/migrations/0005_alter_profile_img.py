# Generated by Django 3.2.3 on 2021-06-09 20:19

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=sorl.thumbnail.fields.ImageField(blank=True, default='images/default.jpg', upload_to='images'),
        ),
    ]
