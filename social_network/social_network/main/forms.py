from django import forms # Імпортуємо модуль forms з Django для створення форм
from publications.models import Post, Tag # Імпортуємо моделі Post та Tag із додатку publications
from django.contrib.auth.models import User # Імпортуємо вбудовану модель користувача Django

# Клас для завантаження одразу кількох файлів 
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True # Зміна яка дозволяє вибрати кілька файлів одночасно у полі форми
# Клас для завантаження кількох зображень замість одного
class MultipleField(forms.ImageField):
    # Це спеціальний метод, який автоматично виконується при створенні поля, дозволяє задати власні параметри
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput()) # Якщо не вказано віджет — використовуємо MultipleFileInput
        super().__init__(*args, **kwargs) # Викликаємо конструктор батьківського класу ImageField, щоб ініціалізувати поле з усіма параметрами 
    # Функція clean відповідає за перевірку і очищення даних, які користувач завантажує через форму
    def clean(self, data, initial=None):
        single_file_clean = super().clean # Отримуємо метод очищення зображення з базового класу ImageField
        if isinstance(data, (list, tuple)): #  Якщо передано кілька файлів
            result = [single_file_clean(d, initial) for d in data] # Проходимо по кожному файлу, застосовучи очищення до кожного окремо
        else: #  Якщо один файл    
            result = single_file_clean(data, initial) # Очищуємо один файл
        return result # Повертаємо результат: список очищених файлів або ж один очищений файл


# Форма Django для створення і редагування публікацій 
class PostForm(forms.ModelForm):
    # Вказуємо модель для форми та перелік полів, які будуть доступні для заповнення
    class Meta: 
        model = Post # Вказуємо модель, з якою працюватиме форма
        fields = ["title", "topic", "tags", "content"] # Поля моделі, які включені у форму
    # Поле для введення URL є НЕобов’язкове
    url = forms.URLField( 
        required = False, # поле не є обов’язковим
        label = "Посилання", # підпис поля у формі
        widget=forms.URLInput(attrs={ # Створює поле для введення URL з додатковими HTML-атрибутами
            "placeholder": "Вкажіть посилання до публікації", # підказка у полі вводу
            "id": "field-url" # HTML id для поля
        })
    )
    # Поле для введення назви публікації
    title = forms.CharField(
        max_length = 255, # максимальна довжина тексту
        label = "Назва публікації", # підпис поля
        widget = forms.TextInput(attrs={ # Вказуємо, як буде виглядати текстове поле
            "placeholder": "Напишіть назву публікації", # підказка користувачу
            "id": "field-title" # HTML id поля
        })
    )
    # Поле для теми публікації  є НЕобов’язкове
    topic = forms.CharField( 
        max_length = 255, # максимальна довжина тексту
        required = False, # необов’язкове поле
        label = "Тема публікації", # підпис поля
        widget = forms.TextInput(attrs={ # Вказуємо, як буде виглядати текстове поле
            "placeholder": "Напишіть тему публікації", # підказка користувачу
            "id": "field-topic" # HTML id поля
        })
    )
    # Поле для основного тексту публікації
    content = forms.CharField( 
        label = "", # без підпису
        widget = forms.Textarea(attrs={ # Створює багато­рядкове текстове поле з додатковими HTML-атрибутами
            "placeholder": "Напишіть текст публікації", # підказка для користувача
            "id": "field-text", # HTML id поля
            "class": "text-create", # CSS клас для стилів
        })
    )
    # Поле для вибору кількох тегів
    tags = forms.ModelMultipleChoiceField( 
        queryset=Tag.objects.all(), # усі доступні теги з бази даних
        widget=forms.CheckboxSelectMultiple(attrs={"id": "field-tags"}), # відображення у вигляді чекбоксів з id
        required=False #  необов’язкове поле
    )


# Форма для редагування публікації з додатковими полями, наприклад завантаження зображень
class PostFormEdit(forms.ModelForm):
    # Форма Django для редагування публікації з можливістю додавання зображень
    class Meta(PostForm.Meta): 
        fields = ["title", "topic", "tags", "text", "url"] #
    # Наслідує налаштування з PostForm і вказує, які поля включити у форму
    images = MultipleField(
        required = False, # Поле необов’язкове
        label = "", # без підпису
        widget = MultipleFileInput(attrs = {
        "id": "image-to-post-form", # HTML-id для поля завантаження зображень
        "class": "image-to-post-form", #  CSS-клас для стилізації поля
        "multiple": True # Дозволяє вибрати кілька зображень одночасно
    }))
    # Поле для завантаження одного або кількох зображень
    url = forms.URLField(
        required = False, # Поле необов’язкове
        label = "Посилання", # Підпис поля 
        widget= forms.URLInput( 
        {"placeholder": "Вкажіть посилання до публікації"} # Підказка для користувача
    ))
    # Поле для введення посилання (URL)
    title = forms.CharField(
        max_length= 255, # максимальна довжина тексту
        label = "Назва публікації", # Підпис поля 
        widget= forms.TextInput( # Створює однорядкове текстове поле для введення даних
        {"placeholder": "Напишіть назву публікації"} # Підказка для користувача
    ))
    # Поле для введення назви публікації
    topic = forms.CharField(
        max_length= 255, # максимальна довжина тексту 
        required = False, # Поле необов’язкове
        abel = "Тема публікації", # Підпис до поля форми, що вказує назву поля користувачу
        widget= forms.TextInput( # Створює однорядкове текстове поле для введення даних
        {"placeholder": "Напишіть тему публікації"}  # Підказка для користувача
    ))
    # Необов’язкове поле для теми публікації
    text = forms.CharField(
        label = "", # без підпису
        widget= forms.Textarea( # Основне багаторядкове поле для тексту публікації
        {"placeholder": "Напишіть текст публікації"} # Підказка для користувача
    ))


#  Форма для оновлення даних користувача
class UserUpdateForm(forms.ModelForm):
    # Вказуємо модель User і перелік полів форми з їх HTML-атрибутами для вводу
    class Meta:
        model = User # Зв’язок форми з моделлю користувача
        fields = ['first_name', 'last_name', 'username'] # Поля форми для редагування
        widgets = { # Визначення зовнішнього вигляду полів форми
            'first_name': forms.TextInput(attrs={'class': 'input-name', 'placeholder': "Введіть Ваше ім’я"}), # Поле для імені з підказкою
            'last_name': forms.TextInput(attrs={'class': 'input-name', 'placeholder': "Введіть Ваше прізвище"}), # Поле для прізвища з підказкою
            'username': forms.TextInput(attrs={'class': 'input-name', 'placeholder': "@"}), # Поле для логіна з підказкою
        }

        
