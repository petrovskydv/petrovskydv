# python manage.py shell
from django.contrib.auth.models import User

from main.models import Category, Post, Person

# Переменные
transport_category = Category.objects.create(title='Транспорт', slug='transport')
work_category = Category.objects.create(title='Работа', slug='rabota')
private_thing_category = Category.objects.create(title='Личные вещи', slug='lichnye_veschi')
me = User.objects.get(username='denis')
person = Person.objects.get(user=me)

# Объявления
post = Post(
    title='Land Rover Range Rover, 2007',
    content='Отличный внешний вид и техническое состояние. '
            'Всё работает как положено. 2 комплекта новых колёс 20 радиус. Зима и лето . '
            'Весь переделан под рестайлинг. Всё стоит оригинал .Автомобиль без единого ДТП . ',
    category=transport_category,
    seller=person
)
post.save()

Post.objects.create(
    title='Пекарь кассир',
    content=''' Требуются продавцы в сеть мини-пекарен "Бон Багет "
График работ сменный 2/2, 3/1.
Обязанности:
-обслуживание покупателей согласно требованиям компании;
-выпечка хлебобулочных изделий без замеса (заморозка);
Требования:
- Аккуратность;

    ''',
    category=work_category,
    seller=person
)

Post.objects.create(
    title='Рюкзак-кенгуру babybjorn',
    content=''' BABYBJORN рюкзак-кенгуру One Air Mesh 2018 обеспечит эргономичность в ношении ребёнка и максимальный комфорт как для вас, так и для малыша.
Он подходит для детей от рождения приблизительно до трёх лет (от 3,5 кг/53 см до 15 кг/100 см). Этот рюкзак-кенгуру разработан при участии педиатров и обеспечивает необходимую поддержку для головы, спины и ног ребёнка. Мы надеемся, что вам и вашему малышу понравится это изделие,
и будем рады получить ваши вопросы и комментарии.
    ''',
    category=private_thing_category,
    seller=person
)

# Запросы
posts_transport = Post.objects.filter(category=transport_category)
posts_work = Post.objects.filter(category=transport_category)
posts_number = person.posts_number
persons_posts = person.sellers_posts.all()
