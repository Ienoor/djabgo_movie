from datetime import date
from django.db import models


class Category(models.Model):
    '''Категории'''

    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Опмсание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    '''Актеры и Режисёры'''

    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Опмсание")
    image = models.ImageField("Изображения", upload_to="actors/")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Актеры и Режисёры"
        verbose_name_plural = "Актеры и Режисёры"


class Gerne(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Опмсание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    '''Фильмы'''

    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Опмсание")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(
        Actor, verbose_name="Режисёр", related_name="film_director")
    actors = models.ManyToManyField(
        Actor, verbose_name="Актрёры", related_name="film_actors")
    ganre = models.ManyToManyField(Gerne, verbose_name="Жанры")
    word_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(
        "Бюджет", default=0, help_text="Указать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0, help_text="Указать сумму в долларах")
    fees_in_word = models.PositiveIntegerField(
        "Сборы в мире", default=0, help_text="Указать сумму в долларах")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("черновик", default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class MovieShorts(models.Model):
    '''Кадры из фильма'''

    name = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Опмсание")
    image = models.ImageField("Изображения", upload_to="movie_shorts/")
    mobie = models.ForeignKey(Movie, verbose_name="Фильмы", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"

class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self) -> str:
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

class Rating(models.Model):
    '''Рейтинг'''

    ip = models.CharField("IP адрес", max_length=16)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.star} {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



