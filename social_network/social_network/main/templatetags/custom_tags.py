# Імпортуємо модуль template з Django 
from django import template 
# Реєструємо бібліотеку шаблонних тегів 
register = template.Library()
# Створюємо декоратор для реєстрації функції як шаблонного фільтра
@register.filter
# Визначаємо функцію, яка отримує значення за ключем із словника
def get_item(dictionary, key):
    # Повертаємо значення зі словника за вказаним ключем
    return dictionary.get(key) 
