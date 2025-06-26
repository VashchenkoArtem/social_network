# Імпортуємо форми з джанго
from django import forms
# Імпортуємо модель користувача з джанго
from django.contrib.auth.models import User
# Імпортуємо моделі Album та Tag з сторінки публікацій
from publications.models import Album, Tag

# Створюємо форму для редагування інформації користувача
class RedactUserForm(forms.ModelForm):
    # Вказуємо класс Meta щоб визначити які данні в моделі є "метадані"
    class Meta:
        # Вказуємо модель User
        model = User
        # Вказуємо поля які будуть використовуватись у формі
        fields = ['first_name', 'last_name', 'email']

# Створюємо форму для створення альбому
class CreateAlbumForm(forms.ModelForm):
     # Вказуємо класс Meta щоб визначити які данні в моделі є "метадані"
    class Meta:
        # Вказуємо модель Album
        model = Album
        # Вказуємо поля які будуть використовуватись у формі
        fields = ['name', 'topic']
    # Створюємо поле name та вказуємо його параметри
    name = forms.CharField(max_length = 255, widget = forms.TextInput(attrs = {
        # Вказуємо класс поля
        'class': 'first-input',
        # Вказуємо текст-підказку для цього поля
        'placeholder': 'Настрій'
    }))
    # Створюємо поле name та вказуємо що користувач може вибрати його наповнення з наданих варіантів
    topic = forms.SelectMultiple(
    )