from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Название в виде url', max_length=200)

    class Meta:
        ordering = ['title']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь', )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.user.username

    @property
    def posts_number(self):
        return self.sellers_posts.count()


class Post(models.Model):
    title = models.CharField('Назание',max_length=50)
    content = models.TextField('Описание',null=True, blank=True)
    price = models.PositiveIntegerField('Цена', default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
        related_name='categories_posts'
    )
    seller = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='продавец',
        related_name='sellers_posts'
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='posts',
        verbose_name='Теги',
        blank=True
    )

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return f'{self.title} - {str(self.seller)}'


class Tag(models.Model):
    title = models.CharField('Тег', max_length=20, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title
