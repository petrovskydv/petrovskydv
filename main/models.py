from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Содержит описание категории."""

    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Название в виде url', max_length=200)

    class Meta:
        ordering = ['title']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Person(models.Model):
    """Содержит автора объявлений, связана с моделью :model:`auth.User`."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь', )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.user.username

    @property
    def posts_number(self):
        """Возвращает количество опубликованных объявлений продавца."""
        return self.sellers_posts.count()


class Post(models.Model):
    """
    Содержит объявление, связано с моделями
    :model:`main.Category`
    :model:`main.Person`
    :model:`main.Tag`
    """

    title = models.CharField('Название', max_length=50)
    content = models.TextField('Описание', null=True, blank=True)
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
    created = models.DateTimeField('дата создания', auto_now_add=True, null=True)
    edited = models.DateTimeField('дата редактирования', auto_now=True, null=True)

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return f'{self.title} - {str(self.seller)}'


class Tag(models.Model):
    """Содержит тэги объявлений."""

    title = models.CharField('Тег', max_length=20, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title
