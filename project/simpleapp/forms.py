from django.forms import ModelForm, BooleanField
from .models import Product


# Создаём модельную форму
class ProductForm(ModelForm):
    # добавляем галочку, или же true-false поле
    check_box = BooleanField(label='Ало, Галочка!')

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля.
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'quantity', 'check_box']
