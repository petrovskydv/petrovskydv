# Generated by Django 3.2.3 on 2021-05-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210526_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания'),
        ),
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='дата редактирования'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]