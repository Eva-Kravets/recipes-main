from django.db import models
from user.models import User


class Calories(models.Model):
    squirrels = models.FloatField(verbose_name='Белки')
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')

    def __str__(self):
        return f'{self. squirrels} {self.fats} {self.carbohydrates}'

    class Meta:
        verbose_name = 'Калории'
        verbose_name_plural = 'Калории'


class Ingredient(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    calories = models.ForeignKey(Calories, verbose_name='Калории', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/ingredients')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Recipe(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name='Категории')
    ingredients = models.ManyToManyField(Ingredient,  verbose_name='Ингредиенты')
    text = models.TextField(verbose_name='Текст рецепта')
    visible = models.BooleanField(verbose_name='Виден?', default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name='Рецепт',related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото', upload_to='photos/recipes')

    class Meta:
        verbose_name = 'Фото рецептов'
        verbose_name_plural = 'Фото рецептов'
