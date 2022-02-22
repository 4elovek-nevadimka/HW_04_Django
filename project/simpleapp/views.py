from datetime import datetime

from django.views.generic import ListView, DetailView

from .filters import ProductFilter
from .forms import ProductForm
from .models import Product, Category


class ProductList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    ordering = ['-price']
    # поставим постраничный вывод в один элемент
    paginate_by = 1
    # добавляем форм класс, чтобы получать доступ к форме через метод POST
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        # создаём новую форму, забиваем в неё данные из POST-запроса
        form = self.form_class(request.POST)

        # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
        if form.is_valid():
            form.save()

        # отправляем пользователя обратно на GET-запрос.
        return super().get(request, *args, **kwargs)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
