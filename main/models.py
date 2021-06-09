from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from sorl.thumbnail import ImageField


class BasePost(models.Model):
    """Абстрактная модель объявления, содержит общие поля"""

    title = models.CharField('Название', max_length=50)

    class Meta:
        abstract = True


class Category(BasePost):
    """Содержит описание категории."""

    slug = models.SlugField('Название в виде url', max_length=200)

    class Meta:
        ordering = ['title']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Person(User):
    """Содержит автора объявлений, унаследована от :model:`auth.User`."""

    class Meta:
        proxy = True
        ordering = ('first_name',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username

    @property
    def posts_number(self):
        """Возвращает количество опубликованных объявлений продавца."""
        return self.sellers_posts.count()


class Profile(User):
    birthdate = models.DateTimeField('дата рождения', blank=True, null=True)
    img = ImageField(upload_to='images', blank=True, default='images/default.jpg')

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def get_absolute_url(self):
        return reverse('profile-update', args=[str(self.id)])


class Post(models.Model):
    """
    Модель объявления, содержит общие поля, связано с моделями
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
        related_name='%(class)s_categories_posts'
    )
    seller = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='продавец',
        related_name='%(class)s_sellers_posts'
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='%(class)s_posts',
        verbose_name='Теги',
        blank=True
    )
    created = models.DateTimeField('дата создания', auto_now_add=True, null=True)
    edited = models.DateTimeField('дата редактирования', auto_now=True, null=True)

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

        abstract = True

    def __str__(self):
        return f'{self.title} - {str(self.seller)}'


class PersonalItem(Post):
    """Содержит объявления о продаже вещей"""

    condition_choices = [
        ('new', 'новое'),
        ('used', 'б/у'),
    ]
    condition = models.CharField('состояние', max_length=20, choices=condition_choices, default='used')

    class Meta:
        verbose_name = 'личные вещи'
        verbose_name_plural = 'личные вещи'
        ordering = ['title']


class Car(Post):
    """Содержит объявления о продаже автомобиля"""

    color = models.CharField('цвет', max_length=20)
    brand = models.CharField('марка', max_length=20)
    mileage = models.PositiveIntegerField('пробег')

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])


class Service(Post):
    """Содержит объявления об услугах"""

    contractor_choices = [
        ('private_person', 'частное лицо'),
        ('organization', 'организация'),
    ]
    contractor = models.CharField('вид исполнителя', max_length=20, choices=contractor_choices,
                                  default='private_person')

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
        ordering = ['title']


class ArchivedPost(Service):
    """Архивные объявления."""

    class Meta:
        proxy = True
        ordering = ["created"]
        verbose_name = 'архивное объявление'
        verbose_name_plural = 'архивные объявления'


class Tag(models.Model):
    """Содержит тэги объявлений."""

    title = models.CharField('Тег', max_length=20, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title
