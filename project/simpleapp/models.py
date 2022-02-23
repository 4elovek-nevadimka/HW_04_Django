from django.db import models
from django.core.validators import MinValueValidator


# Создаём модель товара
class Product(models.Model):
    # названия товаров не должны повторяться
    name = models.CharField(max_length=50, unique=True,)
    #
    description = models.TextField()
    # количество товара на складе
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])
    # цена
    price = models.FloatField(validators=[MinValueValidator(0.0, 'Price should be >= 0.0')])
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.quantity}'

    # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
    def get_absolute_url(self):
        return f'/products/{self.id}'


#  Создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'
