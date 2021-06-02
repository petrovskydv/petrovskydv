# Generated by Django 3.2.3 on 2021-06-02 08:37

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, verbose_name='Название в виде url')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'ordering': ('first_name',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания')),
                ('edited', models.DateTimeField(auto_now=True, null=True, verbose_name='дата редактирования')),
                ('contractor', models.CharField(choices=[('private_person', 'частное лицо'), ('organization', 'организация')], default='private_person', max_length=20, verbose_name='вид исполнителя')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_categories_posts', to='main.category', verbose_name='категория')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_sellers_posts', to='main.person', verbose_name='продавец')),
                ('tags', models.ManyToManyField(blank=True, related_name='service_posts', to='main.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуги',
            },
        ),
        migrations.CreateModel(
            name='PersonalItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания')),
                ('edited', models.DateTimeField(auto_now=True, null=True, verbose_name='дата редактирования')),
                ('condition', models.CharField(choices=[('new', 'новое'), ('used', 'б/у')], default='used', max_length=20, verbose_name='состояние')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalitem_categories_posts', to='main.category', verbose_name='категория')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalitem_sellers_posts', to='main.person', verbose_name='продавец')),
                ('tags', models.ManyToManyField(blank=True, related_name='personalitem_posts', to='main.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'личные вещи',
                'verbose_name_plural': 'личные вещи',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания')),
                ('edited', models.DateTimeField(auto_now=True, null=True, verbose_name='дата редактирования')),
                ('color', models.CharField(max_length=20, verbose_name='цвет')),
                ('brand', models.CharField(max_length=20, verbose_name='марка')),
                ('mileage', models.PositiveIntegerField(verbose_name='пробег')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_categories_posts', to='main.category', verbose_name='категория')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_sellers_posts', to='main.person', verbose_name='продавец')),
                ('tags', models.ManyToManyField(blank=True, related_name='car_posts', to='main.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'автомобиль',
                'verbose_name_plural': 'автомобили',
            },
        ),
        migrations.CreateModel(
            name='ArchivedPost',
            fields=[
            ],
            options={
                'verbose_name': 'архивное объявление',
                'verbose_name_plural': 'архивные объявления',
                'ordering': ['created'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.service',),
        ),
    ]
