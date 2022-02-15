from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
    if isinstance(value, str) and isinstance(arg, int):
        return str(value) * arg
    else:
        # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')