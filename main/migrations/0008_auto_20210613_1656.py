# Generated by Django 3.2.3 on 2021-06-13 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_alter_profile_birthdate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'verbose_name': 'картинка', 'verbose_name_plural': 'картинки'},
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='подписчик')),
            ],
            options={
                'verbose_name': 'подписчик',
                'verbose_name_plural': 'подписчики',
            },
        ),
    ]