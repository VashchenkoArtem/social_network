# Project "Social network - Messanger" | Проєкт "Social network - Messanger" 

## Мета створення проєкту | Purpose of the Project
Мета створення цього проєкту — практика з нововивченими складовими модуля Django: Django Forms, Class-Based Views, Django Channels для роботи з веб-сокетами, а також використання Ajax і робота з форматуванням дат у iso-формат. Його головна мета — вдосконалення наших навичок програмування, спільної командної роботи та втілення дизайнерських ідей.

___

The goal of this project is to practice newly learned parts of the Django framework: Django Forms, Class-Based Views, and Django Channels for working with WebSockets. It also includes using Ajax and formatting dates in ISO format. The main aim is to improve our programming skills, learn to work better and effectively as a team, and apply design ideas in practice.

## Навігація | Navigation on README:
- [Мета створення проєкту | Purpose of the Project](#мета-створення-проєкту--purpose-of-the-project)
- [Навігація | Navigation on README:](#навігація--navigation-on-readme)
- [Склад команди | Team members | Developers](#склад-команди--team-members--developers)
- [Структура | Structure of the project](#структура--structure-of-the-project)
- [Функціонал кожного з додатків | Functionality of each application](#функціонал-кожного-з-додатків--functionality-of-each-application)
- [Особливості функціоналу кожного з додатків з прикладом коду | Features of Each App with Code Example](#особливості-функціоналу-кожного-з-додатків-з-прикладом-коду--features-of-each-app-with-code-example)
- [Як встановити та запустити проєкт? | How to install and run the project?](#як-встановити-та-запустити-проєкт--how-to-install-and-run-the-project)
- [Висновок | Conclusion](#висновок--conclusion)


## Склад команди | Team members | Developers

* [**Ващенко Артем**](https://github.com/VashchenkoArtem) — Teamlead
* [**Овчаренко Юлія**](https://github.com/JuliaOvcharenko)
* [**Сафонова Анна**](https://github.com/AnnaSafonova30)
* [**Марков Дмитро**](https://github.com/DmitriyM08)
* [**Харлан Кирило**](https://github.com/KirillKharlan)

___

* [**Vashchenko Artem**](https://github.com/VashchenkoArtem) — Teamlead
* [**Ovcharenko Yuliia**](https://github.com/JuliaOvcharenko)
* [**Safonova Anna**](https://github.com/AnnaSafonova30)
* [**Markov Dmitro**](https://github.com/DmitriyM08)
* [**Kharlan Kyrylo**](https://github.com/KirillKharlan)


## Структура | Structure of the project

* ![](images_for_readme/figma.svg) [Фігджем структура проєкту](https://www.figma.com/board/KYEFp7dDKIrO5GBJwWNcF8/Social_network---Structure-of-the-project?node-id=0-1&t=cvBIJdu1IKlfONmC-1)

___


* ![](images_for_readme/figma.svg) [FigJam structure of the project](https://www.figma.com/board/KYEFp7dDKIrO5GBJwWNcF8/Social_network---Structure-of-the-project?node-id=0-1&t=cvBIJdu1IKlfONmC-1)


## Функціонал кожного з додатків | Functionality of each application

<details>
  <summary><strong>📁 chats</strong></summary>

  ---
  > 📁 chats – Додаток для чатінгу.
  Під час розробки ми працювали з Django Channels, WebSockets та обробкою дат у форматі ICO. Додаток є корисним тим, що будь-який зареєстрований користувач може створювати й використовувати як групові, так і особисті чати.
  ---
  > 📁 chats  – Application for chating. During the development process we work with: django channels, web socets, and dates in iso-format. The application is useful because everyone can create or user group or individual chats. 
  ---
</details>

<details>
  <summary><strong>📁 friends</strong></summary>

  ---
  > 📁 friends –  Сторінка друзів. Під час розробки цього додатку ми реалізовали функціонал надсилання запитів для додавання у друзі, видалення користувачів із друзів, перегляду списку наявних друзів, а також рекомендацій потенційних. Для цього використовувалися класи відображення TemplateView та DeleteView. На сторінці відображаються як користувачі, які вже є вашими друзями, так і ті, кого можна додати до списку друзів.
  --- 
  > 📁 friends  – Friends page.This page lets you send friend requests, remove friends, see your current friends, and get suggestions for new friends. We used special view classes called TemplateView and DeleteView to build these features. On the page, you can see people who are already your friends and people you can add as friends.

</details>

<details>
  <summary><strong>📁 main</strong></summary>

  ---
  > 📁 main – Головна сторінка проєкту.
  > Це додаток із функціоналом створення, редагування та перегляду постів, з можливістю додавати зображення вручну (з комп’ютера локалько) чи за допомогою URL-адреси. 
  
  > Застосунок має сучасний інтерфейс із модальними формами, що зручно відкриваються/закриваються без перезавантаження сторінки. 
  * Основні можливості:
    - створювати публікації через інтерактивну форму.
    - переглядати вміст окремих блоків за допомогою кнопок «три крапки».
    - редагувати вже створені пости: зʼявляється форма, яка автоматично підтягує дані через AJAX.
    - додавати зображеннz з компʼютера або через поле введення URL-адрес.
  
  * Під час відкриття модальних вікон основний контент затемнюється для зручності користувача. Усі взаємодії та зміни в HTML-документі здійснюються за допомогою JavaScript, що дозволяє створювати зручний, динамічний і плавний інтерфейс користувача.

  ---
  > 📁 main  – Main Page of the Project.
  
  > This is an app where you can create, edit, and view posts. You can add images either from your computer or using a URL link.

  > The app has a modern design with modal forms that open and close easily without reloading the page.

  * Main Features:

    * Create posts using an interactive form.

    * View content blocks by clicking the "three dots" button.

    * Edit posts using a form that loads the data automatically with AJAX.

    * Add images from your computer or by typing a URL.

  > When a modal window opens, the rest of the page becomes darker to help you focus. All changes and actions on the page are made using JavaScript, which helps create a smooth and dynamic user experience.
  ---
</details>

<details>
  <summary><strong>📁 publications</strong></summary>

  ---
  > 📁 Додаток для створення та відображення особистих публікацій користувача. Під час розробки було реалізовано створення, редагування та видалення постів. Використовувалися такі класи відображення: CreateView, UpdateView, DeleteView.
  ---
  > 📁 publications  – An app for creating and showing personal posts.
  While working on this app, we made it possible to create, edit, and delete posts. We used view classes such as CreateView, UpdateView, and DeleteView.
  ---
</details>

<details>
  <summary><strong>📁 registration</strong></summary>

  ---
  > 📁 registration – Додаток для реєстрації, верифікації та аутентифікації користувача.
  * Основний функціонал:
    -  Введення тільки пошти без імені користувача: Пошта і пароль. 
    -  Валідація даних форми. 
    -  Класи відображення: CreateView, FormView, LogoutView. 
    -  Моделі: User.
    -  Forms: VerificationForm, AuthorithationForm, RegistrationForm.
  ---
  
  > 📁 registration  – An app for user registration, verification, and authentication.

  * Main features:

    - Enter only email and password (no username).

    - Form data validation.

    - View classes: CreateView, FormView, LogoutView.

    - Model: User.

    - Forms: VerificationForm, AuthorizationForm, RegistrationForm.
   ---
</details>

<details>
  <summary><strong>📁 settings_app</strong></summary>

  ---
  > 📁 settings_app – Додаток для налаштувань профілю користувача та для створення альбомів. 
  ---
  > 📁 settings_app  – Application for user profile settings and for creating albums
  ---
</details>


## Особливості функціоналу кожного з додатків з прикладом коду | Features of Each App with Code Example

<details>
  <summary><strong>📁 chats</strong></summary>

  ---
  - Файл social_network/chats/[consumers.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/chats/consumers.py)
  
    - consumers.py - файл, який обробляє логіку веб-сокет запитів (аналог views.py).
    
    ___

  - Файл social_network/chats/routing.py
  
    - routing.py - Файл для маршрутизації WebSocket запитів (аналог urls.py).
    ```python
      from django.urls import path # Імпортуємо функцію path для створення маршрутів.
      from .consumers import ChatConsumer # Імпортуємо клас, в якому прописана уся логіка WebSocket запитів.

      # Створюємо список з url для обробки WebSocket-запитів.
      ws_urlpatterns = [
          path("chats/all_chats/<int:chat_pk>", ChatConsumer.as_asgi(), name="chat") # Створємо шлях для chats, вказуючи ChatConsumer як асинхронний обробник для WebSocket запиту.
      ]
    ```
    ___

  - Файл social_network/social_network/asgi.py
    - asgi.py - файл для використання у проєкті асинхронності.

```python
    import os
    from django.core.asgi import get_asgi_application
    from channels.routing import ProtocolTypeRouter, URLRouter
    from chats.routing import ws_urlpatterns
    from channels.auth import AuthMiddlewareStack
    '''
    os.environ.setdefault — встановлює змінну середовища, якщо вона ще не задана.

    DJANGO_SETTINGS_MODULE — назва змінної, яка каже Django, який файл налаштувань використовувати.

    'social_network.settings' — шлях до файлу з налаштуваннями.
    '''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

    # Створюємо змінну application (об'єкт додатку)
    application = ProtocolTypeRouter({
        # При http-запиті викликається стандартна функція get_asgi_application(), яка перенаправить запит в urls.py
        'http': get_asgi_application(),
        # При ws-запиті викликається функція, яка відправить запит у routing.py
        'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns)) 
    })
```
  - Файл social_network/chats/static/js/chat.js
    - chat.js - файл для взаємодії клієнта з сервером за протоколом WS.

```javascript
    const chatGroup = document.getElementById("chatGroupId").value // Отримуємо value прихованого input з id групи.

    const socketUrl = `ws://${window.location.host}/chats/all_chats/${chatGroup}`; //  Формуємо URL адресу для WS-з'єднання за поточним хостом

    const socket = new WebSocket(socketUrl); // Ініціалізуємо WebSocket (Створюємо WS-з'єднання)

    const messages = document.getElementById("messages"); // Отримуємо div з усіма повідомленнями.
    const form = document.getElementById("form"); // Отримуємо об'єкт форми повідомлення.
    const dateTime = document.querySelectorAll(".message-time"); // Отримуємо усі об'єкти дати та часу.
    // Перебираємо усі об'єкти дати та часу.
    for (let time of dateTime){
        let dateAndTime = new Date(time.textContent); // Створюємо об'єкт дати та часу, передаючи контент(дату та час) конкретного повідомлення.
        let dateAndTimeLocal = dateAndTime.toLocaleString([], { hour: '2-digit', minute: '2-digit' }); // Локалізуємо дату та час до годин | хвилин.
        time.textContent = dateAndTimeLocal // Передаємо контент зміненного повідомлення.
    } 
    // Перевіряємо відправку повідомлення.
    form.addEventListener("submit", (event) => {
        // Відміняємо стандартну поведінку форми(відправки даних)
        event.preventDefault()
        // Отримуємо value повідомлення користувача.
        let message = document.getElementById("id_message").value
        // Створюємо JSONString та перетворюємо його в string | Відправляємо JSONString на сервер | Відправляємо на клієнт.
        socket.send(JSON.stringify({"message": message}))
        // Очищуємо messageForm без оновлення сторінки
        form.reset()
    })
```
</details>

<details>
  <summary><strong>📁 friends</strong></summary>

___

- Файл social_network/friends/[views.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/friends/views.py)
    - views.py - файл для логіки додатку.

___

- Файл social_network/friends/static/friends/js/[script.js](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/friends/static/friends/js/script.js)
    - scripts.js - js-файл, в якому прописана логіка ajax.
___

</details>

<details>
  <summary><strong>📁 main</strong></summary>
    
  ___

    - Файл social_network/main/templatetags/custom_tags.py
      - custom_tags.py - файл налаштувань customtags.

  ```python
    from django import template # Імпортуємо модуль template з Django для створення власних тегів та фільтрів шаблонів
    # Створюємо змінну, яка позначає бібліотеку шаблонів і дозволяє використовувати наші теги та фільтри в шаблонах.
    register = template.Library()
    # Реєструємо фільтр, який дозволяє отримувати значення з словника за ключем
    @register.filter
    #Створюємо функцію, яка приймає словник та ключ, і повертає значення за цим ключем
    def get_item(dictionary, key):
        return dictionary.get(key) # Повертає значення за ключем, якщо ключ існує, або None, якщо ключ відсутній
  ```
___

  - Файл social_network/main/[forms.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/main/forms.py)
    - forms.py - файл для створення кастомних валідованих форм django.
    ___

  - Файл social_network/main/[views.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/main/views.py)
    - views.py - файл для логіки додатку.
</details>

<details>
  <summary><strong>📁 publications</strong></summary>
    
  ___

  - Файл social_network/publications/[views.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/publications/views.py)
  - views.py - файл для логіки додатку.
  
  ___
  

  - Файл social_network/publications/[models.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/publications/models.py)
    - models.py -  У файлі models.py ми визначаємо всі об'єкти, що називаються моделі - Models. Вона містить основні поля та поведінку даних, які ви зберігаєте.
  
  ___

  - Файл social_network/publications/static/js/my_publications/[script.js](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/publications/static/js/my_publications/script.js)
    - script.js - js-файл, в якому прописана логіка ajax.
</details>

<details>
  <summary><strong>📁 registration</strong></summary>
    
  ___

  - Файл social_network/registration/[views.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/registration/views.py)
    - views.py - файл для логіки додатку.
  
  ___
  
  - Файл social_network/registration/backends.py
    - backends.py - файл для зміни логіки реєстрації та аутентифікації з "ім'я - пошта - пароль" на "пошта - пароль".
  
```python
  from django.contrib.auth.models import User # Імпортуємо модель User
  from django.contrib.auth.backends import ModelBackend # Імпортуємо звичайні налаштування backend

  # Створюємо клас особливого налаштування backend
  class LoginEmail(ModelBackend):
      # Перестворюємо функцію authenticate
      def authenticate(self, request, username = None, password = None, **kwargs):
          try: # Створюємо оператор try-except
              user = User.objects.get(email=username) # Знаходимо користувача не по ім'ю, а по пошті
              if user.check_password(password): # Перевіряємо пароль
                  return user # Повертаємо користувача 
          except User.DoesNotExist: # Якщо юзер не знайдений 
              return None # Повертаємо None
```
  ___

  - Файл social_network/registration/[forms.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/registration/forms.py)
    - forms.py - файл для створення кастомних валідованих форм django..
  
  ___

  
</details>

<details>
  <summary><strong>📁 settings_app</strong></summary>
    
  ___

  - Файл social_network/settings_app/[views.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/settings_app/views.py)
  - views.py - файл для логіки додатку.
  
  ___

  - Файл social_network/settings_app/[models.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/settings_app/models.py)
    - models.py -  У файлі models.py ми визначаємо всі об'єкти, що називаються моделі - Models. Вона містить основні поля та поведінку даних, які ви зберігаєте.
  
  ___

  - Файл social_network/settings_app/[forms.py](https://github.com/VashchenkoArtem/social_network/blob/master/social_network/settings_app/forms.py)
    - forms.py - файл для створення кастомних валідованих форм django.


</details>




## Як встановити та запустити проєкт? | How to install and run the project?


> [!NOTE]
> Проєкт стабільно працює на Python 3.8 і вище. Для максимальної сумісності та стабільної роботи рекомендуємо використовувати останню доступну версію Python.
> 
> The project works well with Python 3.8 or higher. To be sure everything works correctly, we recommend using the latest version of Python.



<details>
  <summary><strong>
  
  ![](images_for_readme/windows.svg)
  Для Windows | For Windows</strong></summary>

  - 1️⃣ Завантажте та налаштуйте **Python**: Перейдіть на [офіційний сайт Python](https://www.python.org/), знайдіть вкладку ["Downloads"](https://www.python.org/downloads/) і завантажте версію Python відповідно до вашої операційної системи. Під час налаштування обов’язково оберіть опцію "Add python.exe to PATH".
  ___
  - 1️⃣ Download and install **Python**: Go to the [official Python website](https://www.python.org/), open the ["Downloads"](https://www.python.org/downloads/) tab, and download the Python version for your operating system. When installing, make sure to check the box that says "Add python.exe to PATH".

___
  
  ![](images_for_readme/python.jpg)
  ___

  - 2️⃣ Завантажте та налаштуйте **Git**: Перейдіть на [офіційний сайт Git](https://git-scm.com/) і завантажте версію Git відповідно до вашої операційної системи.

  ___

  - 2️⃣ Download and install **Git**: Go to the [official Git website](https://git-scm.com/) and download the version of Git for your operating system.

  ___

  - 3️⃣ Завантажте та налаштуйте **Visual Studio Code**: Перейдіть на [офіційний сайт Visual Studio Code](https://code.visualstudio.com/) 
  
  ___

  - 3️⃣ Download and install Visual Studio Code: Go to the [official Visual Studio Code website](https://code.visualstudio.com/) and download the version for your operating system.

  ___

  - 4️⃣ Відкрийте Visual Studio Code, створіть або відкрийте необхідну папку в якій буде знаходитися проєкт.
  ___

  - 4️⃣ Open Visual Studio Code, then create or open the folder where your project will be.
  
    - Відкрийте термінал, оберіть "Git Bash"
  
    - Open the terminal and choose "Git Bash"
  
    ![](images_for_readme/bash.jpg)
    ___

    - Скопіюйте команду у відкритий термінал:
  
    - Copy the command into the open terminal:
  
      ```sh
      git clone https://github.com/VashchenkoArtem/social_network.git
      ```
    - Створіть віртуальне оточення та активуйте його
    ___

    - Create a virtual environment and activate it

      ```sh
      python -m venv <namevenv>
      ```

      ```sh
      .\<namevenv>\Scripts\activate.bat
      ```

    - Встановіть необхідні бібліотеки в віртуальне оточення з файлу requirements.txt
      
    ___

    - Install the required libraries into the virtual environment from the requirements.txt file

      ```sh
      pip install -r requirements.txt
      ```
      
    - Завантажте channels та daphne для роботи з Django Channels
    ___

    - Install Channels and Daphne for Django Channels

      ```sh
      pip install channels, daphne
      ```
    
    - Перейдіть у папку social_network, в якій знаходиться файл manage.py якщо ви не там

    ___

    - Go to the folder social_network where the manage.py file is, if you are not there yet
  

      ```sh
      cd social_network
      ```

        ```sh
      cd social_network
      ```

    - Проведіть міграції
    ___

    - Run the migrations
  
      ```sh
      python manage.py migrate
      ```

    - Запустіть сервер
    ___
    - Run the project
  
      ```sh
      python manage.py runserver
      ```
  - 5️⃣ Вітаємо! Ви локально запустили проєкт!
  ___
  - 5️⃣ Congratulations! You have successfully run the project locally!
</details>


<details>
  <summary><strong>
  
  ![](images_for_readme/macos.svg)
  Для MacOS | For MacOS</strong></summary>


  - 1️⃣ Завантажте та налаштуйте **Python**: Перейдіть на [офіційний сайт Python](https://www.python.org/), знайдіть вкладку ["Downloads"](https://www.python.org/downloads/) і завантажте версію Python відповідно до вашої операційної системи. Під час налаштування обов’язково оберіть опцію "Add python.exe to PATH".
  ___
  - 1️⃣ Download and install **Python**: Go to the [official Python website](https://www.python.org/), open the ["Downloads"](https://www.python.org/downloads/) tab, and download the Python version for your operating system. When installing, make sure to check the box that says "Add python.exe to PATH".

___
  
  ![](images_for_readme/python.jpg)
  ___

  - 2️⃣ Завантажте та налаштуйте **Git**: Перейдіть на [офіційний сайт Git](https://git-scm.com/) і завантажте версію Git відповідно до вашої операційної системи.

  ___

  - 2️⃣ Download and install **Git**: Go to the [official Git website](https://git-scm.com/) and download the version of Git for your operating system.

  ___

  - 3️⃣ Завантажте та налаштуйте **Visual Studio Code**: Перейдіть на [офіційний сайт Visual Studio Code](https://code.visualstudio.com/) 
  
  ___

  - 3️⃣ Download and install Visual Studio Code: Go to the [official Visual Studio Code website](https://code.visualstudio.com/) and download the version for your operating system.

  ___

  - 4️⃣ Відкрийте Visual Studio Code, створіть або відкрийте необхідну папку в якій буде знаходитися проєкт.
  ___

  - 4️⃣ Open Visual Studio Code, then create or open the folder where your project will be.
  
    - Відкрийте термінал, оберіть "Git Bash"
    - 
    - Open the terminal and choose "Git Bash"
  
    ![](images_for_readme/bash.jpg)
    ___

    - Скопіюйте команду у відкритий термінал:
  
    - Copy the command into the open terminal:

    ```sh
      git clone https://github.com/VashchenkoArtem/social_network.git
    ```
    - Створіть віртуальне оточення та активуйте його
    ___

    - Create a virtual environment and activate it

      ```sh
      python3 -m venv <namevenv>
      ```

      ```sh
      source <namevenv>/bin/activate
      ```

    - Встановіть необхідні бібліотеки в віртуальне оточення з файлу requirements.txt
      
    ___

    - Install the required libraries into the virtual environment from the requirements.txt file

      ```sh
      pip install -r requirements.txt
      ```

    - Завантажте channels та daphne для роботи з Django Channels
    ___

    - Install Channels and Daphne for Django Channels

      ```sh
      pip install channels, daphne
      ```
    
    - Перейдіть у папку social_network, в якій знаходиться файл manage.py якщо ви не там

    ___

    - Go to the folder social_network where the manage.py file is, if you are not there yet
  

      ```sh
      cd social_network
      ```

        ```sh
      cd social_network
      ```

    - Проведіть міграції
    ___

    - Run the migrations
  
      ```sh
      python3 manage.py migrate
      ```

    - Запустіть сервер
    ___
    - Run the project
  
      ```sh
      python3 manage.py runserver
      ```
    ___

    - Натисніть на посилання

    ___

    - Click on link
  
  - 5️⃣ Вітаємо! Ви локально запустили проєкт!
  ___
  - 5️⃣ Congratulations! You have successfully run the project locally!
</details>

___

### Висновок | Conclusion 
📱 Проєкт social_network — проєкт, який навчив нас злагодженій роботі у команді та став важливим етапом у поглибленному вивченні Django. 
У процессі розробки ми:
- Застосовували Django Forms, Class-Based Views, Django Channels для роботи з вебсокетами.
- Реалізували Ajax-запити та попрацювали з форматуванням дат у ISO-формат.
- Познайомилися з поняттями реляційних і нереляційних баз даних, використовуючи:

  - ![](images_for_readme/database.svg) SQLite — для локальної розробки.
  - ![](images_for_readme/database.svg) MySQL — для глобального використання.
  
  ___

- ![](images_for_readme/figma.svg) Окрему увагу було приділено втіленню дизайнерських ідей — важлива навичка frontend-розробки.
  - Верстання з використанням функції calc() та одиниць виміру vw / vh
  - Адаптивний дизайн, максимально наближений до запропонованого макету.

- 🤝 Командна робота
  - Для забезпечення ефективної та комфортної роботи у команді ми дотримувалися таких принципів:

  - 🔧 Чіткий розподіл задач — кожен учасник відповідав за свій функціонал згідно з розподілом, наданим Team Lead.
  - 📞 Регулярна комунікація — обговорення у відео-чаті загальних проблем написаного коду та його функціоналу, видача тімлідом задач для участників групи. Зустрічі відбувалися щонайменше двічі на тиждень.

  - 🌐 Робота з Git — Усі учасники активно використовували систему контролю версій: створення гілок, злиття, зберігання коду.

  - 🌐 Робота з Github — кожен учасник має власну гілку на [гітхаб-репозиторії](https://github.com/VashchenkoArtem/social_network), виконуючи завдання.
  
- 🛠️ Використані технології
  - У процесі розробки були використані такі технології та інструменти:
  - Python – Основна мова програмування, на якій реалізована серверна логіка проєкту.
  
  - Django — Python фреймворк для швидкої та безпечної розробки веб-додатків. 
  
  - JavaScript — Мова програмування для створення функціоналу, інтерактивності та "краси" на стороні користувача.
  
  - HTML — Мова-конструктор, на якому побудована структура всіх веб-сторінок проекту.
  
  - CSS – Мова, яка відповідає за зовнішній вигляд сторінок: кольори, шрифти, розміщення елементів і «косметичний» функціонал.
  
  - jQuery — JavaScript-бібліотека, яка має спрощені методи для роботи з Ajax.
  
  - SQLite – Реляційна база даних для локальної роботи.
  
  - MySQL — Реляційна база даних для віддаленої роботи.
  
  - Git – Система контролю версій	для відстеження змін у коді.
  
  - GitHub — Онлайн-платформа для збереження Git-проєктів та спільної роботи, публікації, обговорення коду.
  
  - [Figma](https://www.figma.com/design/20TZphWNufeAQYOe7E1sze/%D0%A1%D0%BE%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0-%D0%BC%D0%B5%D1%80%D0%B5%D0%B6%D0%B0-World-IT?node-id=6-26&p=f&t=bGAjDfyxAR23sLlY-0)
  
  - Markdowm — легка, але обмежена мова розмітки, яка дозволяє швидко оформлювати текст: робити заголовки, списки, виділення, вставляти зображення чи посилання. Команда використовувала для написання README.md.


🎯 Завершивши цей проєкт, ми отримали досвід, пов'язаний із покращенням нововивчених складових модуля Django: Django Forms, Class-Based Views, Django Channels для роботи з веб-сокетами, а також використання Ajax і робота з форматуванням дат у iso-формат. Ми отримали навички злагодженної командної роботи, підготовали веб-застосунок до використання з n-кількістю реальних користувачів. Також наша команда дізналася як працювати із віддаленими базами даних на прикладі MySQL. 

⚠️ Труднощі розробки:
- Неправильний розподіл свого часу — проєкт розроблявся наприкінці навчального року, під час контрольних та тестів | виділення на дипломний проєкт 1,5 місяці.
- Проблеми з роботою дат у iso-форматі.
- Робота з віддаленною Базою Даних
- Оптимізацію запитів до Бази Даних
___



📱 Project "social_network"
The social_network project helped us learn how to work together as a team. It was an important step in learning more about Django.

During the project, we:
  - Used Django Forms, Class-Based Views, and Django Channels to work with WebSockets.

  - Used Ajax requests and worked with ISO date format.

  - Learned about relational and non-relational databases:

    - ![](images_for_readme/database.svg) SQLite – for local work.

    - ![](images_for_readme/database.svg) MySQL – for global use.

![](images_for_readme/figma.svg) Design
  - We paid special attention to design ideas — this is an important skill for frontend development.
  - We used:

    - The calc() function and CSS units like vw, vh.
  - Responsive design to make the site look good on all screens.

🤝 Teamwork
We worked as a team. To do this, we:

  - 🔧 Shared the tasks — each person had their part of the project.

  - 📞 Talked often — we had video calls at least two times a week.

  - 🌐 Used Git — we created branches, saved our work, and worked together.

  - 🌐 Used GitHub — each person had their own branch in the GitHub repository.
  
🛠️ Used Technologies

  - During the development, the following technologies and tools were used:

  - Python – The main programming language used for the project’s backend logic.

  - Django – A Python framework for fast and secure web application development.

  - JavaScript – A programming language used to create functionality, interactivity, and "beauty" on the user’s side.

  - HTML – A markup language that builds the structure of all web pages in the project.

  - CSS – A language that controls the look of pages: colors, fonts, layout, and cosmetic functions.

  - jQuery – A JavaScript library that makes working with Ajax easier.

  - SQLite – A relational database for local work.

  - MySQL – A relational database for remote work.

  - Git – A version control system to track changes in the code.

  - GitHub – An online platform to store Git projects, work together, publish, and discuss code.

  - Figma – A design tool used by the team for creating UI and layouts.

  - Markdown – A simple but limited markup language that helps quickly format text: create headings, lists, highlights, insert images or links. The team used it for writing the README.md file.


🎯 What We Learned
After this project:

  - We know more about Django: Django Forms, Class-Based Views, WebSockets, Ajax, and date formats.

  - We know how to work in a team and build a web app for real users.

  - We learned how to use remote databases like MySQL.

⚠️ Challenges
  - Time management — the project was during the school year — all teammate had exams. | We had only 1.5 months to finish it.
  - There were problems with ISO date format.
