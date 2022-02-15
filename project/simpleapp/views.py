from django.views.generic import ListView, DetailView
from .models import Product


class ProductList(ListView):
    # указываем модель, объекты которой мы будем выводить
    model = Product
    # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    template_name = 'products.html'
    # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'