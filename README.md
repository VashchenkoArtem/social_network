# Project "Social network - Messanger" | Проєкт "Social network - Messanger" 

## Навігація | Navigation on README:
- [Мета створення проєкту | Purpose of the Project](#мета-створення-проєкту--purpose-of-the-project)
- [Склад команди | Team members | Developers](#склад-команди--team-members--developers)
- [Посилання | Links](#посилання--links)
- [Структура | Structure of the project](#структура--structure-of-the-project)
- [Функціонал кожного з додатків | Functionality of each application](#функціонал-кожного-з-додатків--functionality-of-each-application)
- [Особливості функціоналу кожного з додатків з прикладом коду | Features of Each App with Code Example](#особливості-функціоналу-кожного-з-додатків-з-прикладом-коду--features-of-each-app-with-code-example)
- [Як встановити та запустити проєкт? | How to install and run the project?](#як-встановити-та-запустити-проєкт--how-to-install-and-run-the-project)
- [Висновок | Conclusion](#висновок--conclusion)

  
## Мета створення проєкту | Purpose of the Project
Мета створення цього проєкту — практика з нововивченими складовими модуля Django: Django Forms, Class-Based Views, Django Channels для роботи з веб-сокетами, а також використання Ajax і робота з форматуванням дат у iso-формат. Його головна мета — вдосконалення наших навичок програмування, спільної командної роботи та втілення дизайнерських ідей.

___

The goal of this project is to practice newly learned parts of the Django framework: Django Forms, Class-Based Views, and Django Channels for working with WebSockets. It also includes using Ajax and formatting dates in ISO format. The main aim is to improve our programming skills, learn to work better and effectively as a team, and apply design ideas in practice.

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

## Посилання | Links

* ![](images_for_readme/figma.svg) [Фігма дизайн](https://www.figma.com/design/20TZphWNufeAQYOe7E1sze/%D0%A1%D0%BE%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0-%D0%BC%D0%B5%D1%80%D0%B5%D0%B6%D0%B0-World-IT?node-id=6-26&p=f&t=bGAjDfyxAR23sLlY-0)

___

* ![](images_for_readme/figma.svg) [Figma design](https://www.figma.com/design/20TZphWNufeAQYOe7E1sze/%D0%A1%D0%BE%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0-%D0%BC%D0%B5%D1%80%D0%B5%D0%B6%D0%B0-World-IT?node-id=6-26&p=f&t=bGAjDfyxAR23sLlY-0)



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
  - Файл social_network/chats/consumers.py
  
    - consumers.py - файл, який обробляє логіку веб-сокет запитів (аналог views.py).
  
    ```python

      from channels.generic.websocket import AsyncWebsocketConsumer # Імпортуємо AsyncWebsocketConsumer - клас у Django Channels, який дозволяє створювати асинхронні WebSocket-з'єднання між сервером і браузером у реальному часі.
      import json # Імпортуємо json для майбутньої передачі text_data у javascript.
      from .forms import MessageForm # Імпортуємо форму для відправки валідованих повідомленнь.
      from channels.db import database_sync_to_async, sync_to_async # Імпортуємо декоратор database_sync_to_async для асинхронної роботи бази даних та декоратор sync_to_async для створення асинхронних методів.
      from .models import ChatGroup, ChatMessage # Імпортуємо моделі для роботи з кімнатами чатів та для повідомлень.
      from settings_app.models import Profile, Avatar # Імпортуємо моделі для роботи з користувачем.
      from django.core import serializers # Імпортуємо модуль serializers, щоб використовувати функцію serialize для форматування python-рядка у json-рядок.

      # Створили клас ChatConsumer, який відповідає за з'єднання сервера с клієнтом. Він відловлює запити та обробляє їх.
      class ChatConsumer(AsyncWebsocketConsumer):
          # Створюємо асинхронний метод connect, який відпрацьовує після запиту про підключення.
          async def connect(self):
              self.chat_pk = str(self.scope["url_route"]["kwargs"]["chat_pk"]) # Отримуємо id групи з динамічного поточного URL під ім'ям "chat_pk".
              self.group_name = self.chat_pk # Створюємо назву поточному чату.

              # Під'єднуємо поточного користувача (тобто його канал) до групи, котра вказана в динамічному URL.
              await self.channel_layer.group_add(
                  self.group_name, self.channel_name
              )

              # Запит про підключення схвалений.
              await self.accept()

          # Створюємо асинхронний метод receive, який відпрацьовує коли сервер отримує повідомленя від клієнта.
          async def receive(self, text_data):
              self.user = self.scope["user"] # Отримуємо поточного користувача.
              username = self.user.username # Отримуємо ім'я поточного користувача.
              id = self.user.id # Отримуємо id поточного користувача.
              avatars = await self.get_avatars() # Викликаємо асинхрону функцію get_avatars для отримання всіх аватарів.
              profile = await self.get_profile() # Викликаємо асинхрону функцію get_profile для отримання всії профілів.
              saved_message = await self.save_message(message = json.loads(text_data)['message']) # Зберігаеємо повідомлення у базу даних та у змінну "saved_message".
              # Відправляємо повідомлення всім участникам групи.
              await self.channel_layer.group_send(self.group_name,
                  {
                      "type": "send_message_to_chat", # Вказуємо тип обробника (метод, що викличиться для відправки повідомлення).
                      "text_data": text_data, # Передаємо повідомлення користувача через event, send_message_to_chat.
                      "username": username, # Передаємо користувача(автора повідомлення).
                      "date_time": saved_message.sent_at, # Передаємо час відправки повідомлення.
                      "user_id": id, # Передаємо id поточного користувача.
                      "all_avatars": avatars, # Передаємо аватар користувача.
                      "profile_id":profile # Передаємо профіль користувача.
                  })
              
          # Створюємо асинхронний метод відправки повідомлення до чату.
          async def send_message_to_chat(self, event):
              text_data_dict = json.loads(event['text_data']) # Перетворюємо текст з формату json у python словник.
              form = MessageForm(text_data_dict) # Передаємо дані у форму для валідації
              username = event['username'] # Отримуємо username поточного користувача
              text_data_dict['username'] = username # Записуємо ім'я поточного користувача до словника у форматі json, щоб отримати та використати у js.
              '''
              Записуємо дату та час відправлення повідомлення до словника у форматі json, 
              щоб отримати та використати у js. Використовуємо функцію isoformat() для переведення дати у iso-формат, 
              щоб локалізувати час у файлі chat.js
              '''
              text_data_dict['date_time'] = event['date_time'].isoformat()
              text_data_dict['user_id'] = event['user_id'] # Записуємо id поточного користувача до словника у форматі json, щоб отримати та використати у js.
              text_data_dict['profile_id'] = event['profile_id'] # Записуємо профіль поточного користувача до словника у форматі json, щоб отримати та використати у js.
              
              if form.is_valid(): # Якщо форма валідна(повідомлення проходить валідацію).
                  await self.send(json.dumps(text_data_dict)) # Відправляємо повідомлення користувачу у форматі json для роботи у chat.js.
          
          # Використовуємо декоратор database_sync_to_async для асинхронної роботи бази даних.
          @database_sync_to_async
          # Створюємо функцію для збереження повідомлення.
          def save_message(self, message):
              content = message # Передаємо контент повідомлення.
              author = Profile.objects.get(user = self.scope["user"]) # Передаємо автора поточного повідомлення.
              group = ChatGroup.objects.get(pk = self.group_name) # Отримуємо поточну групу, у яку потрібно зберігати повідомлення.
              return ChatMessage.objects.create(content = content, author = author, chat_group = group) # Повертаємо створене повідомлення
          
          # Використовуємо декоратор sync_to_async для створення асинхронних методів.
          @sync_to_async
          # Створюємо метод, який потрібен для отримання усіх аватарів.
          def get_avatars(self):
              all_avatars = Avatar.objects.all() # Отримуємо всі аватари.
              return json.loads(serializers.serialize("json", all_avatars)) # Перероблюємо та повертаємо отриманні дані у json-формат для роботи із chat.js.
          
          # Використовуємо декоратор sync_to_async для створення асинхронних методів.
          @sync_to_async
          # Створюємо метод, який потрібен для отримання усіх профілів.
          def get_profile(self):
              self.user = self.scope["user"] # Отримуємо поточного користувача.
              id = self.user.id # Отримуємо id користувача
              profile_id = Profile.objects.get(user_id = id) # Отримуємо усі профілі.
              return profile_id.id # Повертаємо id усіх профілів.
              
    ```
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
  ___


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

  ---
</details>

<details>
  <summary><strong>📁 friends</strong></summary>

  ___

  - Файл social_network/friends/views.py
    - views.py - файл для логіки додатку.

```python
  import profile # Імпортуємо профіль
  from django.shortcuts import render, redirect # Імпортуємо функції для рендерингу та редіректу
  from django.views.generic import TemplateView, DeleteView # Імпортуємо класи для роботи з шаблонами та видаленням
  from settings_app.models import Profile, Friendship, Avatar # Імпортуємо моделі профілю, дружби та аватара
  from publications.models import Album # Імпортуємо модель альбому
  from publications.models import Post # Імпортуємо модель посту
  from django.urls import reverse_lazy # Імпортуємо функцію для зворотного редіректу
  from django.shortcuts import get_object_or_404 # Імпортуємо функцію для отримання об'єкта або 404 помилки
  from django.contrib.auth.models import User # Імпортуємо модель користувача

  # Створюємо клас для відображення друзів
  class FriendsView(TemplateView):
      template_name = "friends/friends.html" # Вказуємо шаблон для відображення друзів
      #Створюємо метод для отримання контексту даних
      def get_context_data(self, **kwargs): 
          context = super(FriendsView, self).get_context_data(**kwargs) # Успадковуємо контекст з батьківського класу
          profile = Profile.objects.get(user = self.request.user) # Отримуємо профіль поточного користувача
          context["all_recommended"] = Profile.objects.filter().exclude(user = self.request.user) # Збираємо всіх користувачів, окрім поточного та передаємо їх у контекст
          context["all_friends"] = Friendship.objects.filter(accepted = True) # Отримуємо всіх друзів, які мають підтверджену дружбу та передаємо їх у контекст
          context["all_requests"] = Friendship.objects.filter(profile2 = profile, accepted = False) # Отримуємо всі запити на дружбу, які надіслані поточному користувачу та передаємо їх у контекст 
          context["all_avatars"] = Avatar.objects.all() # Отримуємо всі аватари користувачів та передаємо їх у контекст
          context["current_user"] = Profile.objects.get(user = self.request.user) # Отримуємо профіль поточного користувача та передаємо його у контекст
          author_avatars = {} # Створюємо словник для зберігання аватарів авторів
          
          for author in Profile.objects.all(): # Перебираємо всіх авторів профілів
              avatar = Avatar.objects.filter(profile=author, shown=True, active=True).first() # Отримуємо перший аватар автора, який показується та активний
              author_avatars[author.id] = avatar # Додаємо аватар автора до словника за його ID
          context["author_avatars"] = author_avatars # Передаємо словник аватарів авторів у контекст
          return context # Повертаємо контекст для використання в шаблоні
      # Створюємо метод для обробки запиту
      def dispatch(self, request, *args, **kwargs):
          if not Profile.objects.filter(user_id = request.user.id).exists(): # Якщо профіль користувача не існує
              return redirect("registration") # Перенаправляємо на сторінку реєстрації
          else:   # Якщо профіль існує
              return super().dispatch(request, *args, **kwargs) # Викликаємо метод dispatch батьківського класу для обробки запиту
              
      
      
  # Створюємо клас для відображення всіх друзів
  class AllFriendsView(TemplateView):
      template_name = "all_friends/all_friends.html" # Вказуємо шаблон для відображення всіх друзів
      # Створюємо метод для отримання контексту даних
      def get_context_data(self, **kwargs):
          context = super(AllFriendsView, self).get_context_data(**kwargs) # Успадковуємо контекст з батьківського класу
          context["all_friends"] = Friendship.objects.filter(accepted = True) # # Отримуємо всіх друзів, які мають підтверджену дружбу та передаємо їх у контекст
          context["all_avatars"] = Avatar.objects.all() # Отримуємо всі аватари користувачів та передаємо їх у контекст
          context["current_user"] = Profile.objects.get(user = self.request.user) # Отримуємо профіль поточного користувача та передаємо його у контекст
          author_avatars = {} # Створюємо словник для зберігання аватарів авторів #
          for author in Profile.objects.all(): # Перебираємо всіх авторів профілів #
              avatar = Avatar.objects.filter(profile=author, shown=True, active=True).first() # Отримуємо перший аватар автора, який показується та активний #
              author_avatars[author.id] = avatar # Додаємо аватар автора до словника за його ID #
          context["author_avatars"] = author_avatars # Записуємо словник аватарів авторів у контекст 
          return context # Повертаємо контекст для використання в шаблоні 
      # Створюємо метод для обробки запиту
      def dispatch(self, request, *args, **kwargs):
          if not Profile.objects.filter(user_id = request.user.id).exists(): # Якщо профіль користувача не існує 
              return redirect("registration") # Перенаправляємо на сторінку реєстрації
          else:  # Інакше, якщо профіль існує
              return super().dispatch(request, *args, **kwargs) # Викликаємо метод dispatch батьківського класу для обробки запиту

  # Створюємо клас для відображення всіх запитів на дружбу
  class RequestView(TemplateView):
      template_name = "all_requests/requests.html" # Вказуємо шаблон для відображення всіх запитів на дружбу
  # Створюємо метод для отримання контексту даних
      def get_context_data(self, **kwargs):
          context = super(RequestView, self).get_context_data(**kwargs) # Успадковуємо контекст з батьківського класу 
          profile = Profile.objects.get(user = self.request.user) # Отримуємо профіль поточного користувача 
          context["all_requests"] = Friendship.objects.filter(profile2 = profile, accepted = False) # Отримуємо всі запити на дружбу, які надіслані поточному користувачу та передаємо їх у контекст
          context["all_avatars"] = Avatar.objects.all() # Отримуємо всі аватари користувачів та передаємо їх у контекст 
          author_avatars = {} # Створюємо словник для зберігання аватарів авторів 
          for author in Profile.objects.all(): # Перебираємо всіх авторів профілів 
              avatar = Avatar.objects.filter(profile=author, shown=True, active=True).first() # Отримуємо перший аватар автора, який показується та активний 
              author_avatars[author.id] = avatar # Додаємо аватар автора до словника за його ID #
          context["author_avatars"] = author_avatars # Записуємо словник аватарів авторів у контекст
          return context # Повертаємо контекст для використання в шаблоні
      # Створюємо метод для обробки запиту
      def dispatch(self, request, *args, **kwargs): 
          if not Profile.objects.filter(user_id = request.user.id).exists(): #Якщо профіль користувача не існує
              return redirect("registration") # Перенаправляємо на сторінку реєстрації
          else: # Якщо профіль існує
              return super().dispatch(request, *args, **kwargs) # Викликаємо метод dispatch батьківського класу для обробки запиту
  # Створюємо клас для відображення рекомендованих користувачів
  class RecommendedView(TemplateView):
      template_name = "recommended/recommended.html" # Вказуємо шаблон для відображення рекомендованих користувачів
      # Створюємо метод для отримання контексту даних
      def get_context_data(self, **kwargs):
          context = super(RecommendedView, self).get_context_data(**kwargs) # Успадковуємо контекст з батьківського класу 
          context["all_recommended"] = Profile.objects.filter().exclude(user = self.request.user) # Збираємо всіх користувачів, окрім поточного та передаємо їх у контекст
          context["all_avatars"] = Avatar.objects.all() # Отримуємо всі аватари користувачів та передаємо їх у контекст
          author_avatars = {} # Створюємо словник для зберігання аватарів авторів 
          for author in Profile.objects.all(): # Перебираємо всіх авторів профілів 
              avatar = Avatar.objects.filter(profile=author, shown=True, active=True).first() # Отримуємо перший аватар автора, який показується та активний #
              author_avatars[author.id] = avatar # Додаємо аватар автора до словника за його ID #
          context["author_avatars"] = author_avatars # Записуємо словник аватарів авторів у контекст
          return context # Повертаємо контекст для використання в шаблоні
      
      # Створюємо метод для обробки запиту
      def dispatch(self, request, *args, **kwargs): 
          if not Profile.objects.filter(user_id = request.user.id).exists(): # Якщо профіль користувача не існує
              return redirect("registration") # Перенаправляємо на сторінку реєстрації
          else: # Якщо профіль існує  
              return super().dispatch(request, *args, **kwargs) # Викликаємо метод dispatch батьківського класу для обробки запиту
  # Створюємо клас для відображення профілю друга
  class FriendProfileView(TemplateView):
      template_name = 'friend_profile/friend_profile.html' #
      def get_context_data(self, **kwargs): #
          context = super(FriendProfileView, self).get_context_data(**kwargs) #
          friend_pk = self.kwargs['friend_pk'] #
          friend_user = User.objects.get(id = friend_pk) # 
          profile_id = Profile.objects.get(user_id = friend_pk) #
          context['friend'] = Profile.objects.get(user_id = friend_pk) #
          context['avatar'] = Avatar.objects.filter(profile = profile_id).first() #
          context['all_avatars'] = Avatar.objects.all() #
          context['all_posts'] = Post.objects.filter(author_id = profile_id.pk).all().order_by('-id') #
          context["posts_count"] = Post.objects.filter(author_id = profile_id.pk).count() #
          context['current_request'] = Friendship.objects.filter(profile1= Profile.objects.get(user = friend_user), profile2 =Profile.objects.get(user = self.request.user)).union(Friendship.objects.filter(profile2= Profile.objects.get(user = friend_user), profile1 =Profile.objects.get(user = self.request.user))).first()
          context['all_views'] = Post.objects.none() #
          context['all_albums'] = Album.objects.filter(author = profile_id) #
          for post in Post.objects.filter(author = profile_id): #
              context['all_views'] = context['all_views'] | post.views.all() #
          context["my_friends"] = Friendship.objects.filter(profile2 = profile_id, accepted = True).union(Friendship.objects.filter(profile1 = profile_id, accepted = True))
          return context #
      #
      def dispatch(self, request, *args, **kwargs):
          if not Profile.objects.filter(user_id = request.user.id).exists():#
              return redirect("registration") #
          else: #
              return super().dispatch(request, *args, **kwargs) #
  # Створюємо функцію для видалення запиту на дружбу
  def delete_request(request, pk):
      current_user = Profile.objects.get(user_id = request.user.id) # Отримуємо профіль поточного користувача
      friend_user = Profile.objects.get(user_id = pk) # Отримуємо профіль користувача, якого потрібно видалити з друзів
      if Friendship.objects.filter(profile1_id = request.user.pk, profile2 = friend_user): # Якщо існує дружба між поточним користувачем та користувачем, якого потрібно видалити
          Friendship.objects.get(profile1 = current_user, profile2 = friend_user).delete() # Видаляємо дружбу між поточним користувачем та користувачем, якого потрібно видалити
      if Friendship.objects.filter(profile2 = current_user, profile1 = friend_user): # Якщо існує дружба між користувачем, якого потрібно видалити, та поточним користувачем
          Friendship.objects.get(profile2 = current_user, profile1 = friend_user).delete() # Видаляємо дружбу між користувачем, якого потрібно видалити, та поточним користувачем
      return redirect("main_friends") # Перенаправляємо на сторінку друзів
  # Створюємо функцію для видалення рекомендованого користувача
  def delete_recommended(request, pk):
      rejected_user = User.objects.get(id = pk) # Отримуємо користувача, якого потрібно видалити з рекомендованих
      return redirect("main_friends") # Перенаправляємо на сторінку друзів
  # Створюємо функцію для видалення друга
  def delete_friend(request, pk):
      current_user = Profile.objects.get(user_id = request.user.id) # Отримуємо профіль поточного користувача 
      friend_user = Profile.objects.get(user_id = pk)# Отримуємо профіль користувача, якого потрібно видалити з друзів 
      if Friendship.objects.filter(profile1 = current_user, profile2 = friend_user): # Якщо існує дружба між поточним користувачем та користувачем, якого потрібно видалити
          Friendship.objects.get(profile1 = current_user, profile2 = friend_user).delete() # Видаляємо дружбу між поточним користувачем та користувачем, якого потрібно видалити
      if Friendship.objects.filter(profile2 = current_user, profile1 = friend_user): #Якщо існує дружба між користувачем, якого потрібно видалити, та поточним користувачем
          Friendship.objects.get(profile2 = current_user, profile1 = friend_user).delete() # Видаляємо дружбу між користувачем, якого потрібно видалити, та поточним користувачем
      return redirect("main_friends") # Перенаправляємо на сторінку друзів
  # Створюємо функцію для підтвердження запиту на дружбу
  def confirm_friend(request, pk):    
      current_profile = Profile.objects.get(user_id = request.user.id) # Отримуємо профіль поточного користувача 
      friend_profile = Profile.objects.get(user_id = pk) # Отримуємо профіль користувача, якого потрібно підтвердити як друга 
      current_user = User.objects.get(id = request.user.id) # Отримуємо користувача, який надіслав запит на дружбу 
      friend_user = User.objects.get(id = pk) # Отримуємо користувача, якого потрібно підтвердити як друга 
      request = Friendship.objects.get(profile1=friend_profile, profile2=current_profile) # Отримуємо запит на дружбу
      request.accepted = True # Задаємо статус запиту на дружбу як підтверджений
      request.save() # Зберігаємо зміни в запиті на дружбу
      return redirect("main_friends") # Перенаправляємо на сторінку друзів
  # Створюємо функцію для надсилання запиту на дружбу
  def request_to_user(request, pk):
      current_user = Profile.objects.get(user_id = request.user.id) # Отримуємо профіль поточного користувача
      request_user = Profile.objects.get(user_id = pk) # Отримуємо профіль користувача, якому надсилається запит на дружбу
      if len(Friendship.objects.filter(profile1 = current_user, profile2 = request_user)) == 0 and len(Friendship.objects.filter(profile1 = request_user, profile2 = current_user)) == 0: # Якщо немає існуючих запитів на дружбу між поточним користувачем та користувачем, якому надсилається запит
          Friendship.objects.create(profile1 = current_user, profile2 = request_user, accepted = False) # Створюємо новий запит на дружбу між поточним користувачем та користувачем, якому надсилається запит
      return redirect("main_friends") # Перенаправляємо на сторінку друзів
```
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


  - Файл social_network/main/forms.py
    - forms.py - файл для створення кастомних валідованих форм django.

```python
  from django import forms # Імпортуємо модуль forms з Django для створення форм.
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
      # Поле для теми публікації є НЕобов’язкове
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
```
  ___

  - Файл social_network/main/views.py
    - views.py - файл для логіки додатку.

```python
  from django.views.generic.edit import CreateView, DeleteView, UpdateView # Імпортуємо класи для створення, видалення та редагування об'єктів
  from django.views.generic import View # Імпортуємо клас для створення власних представлень
  from .forms import PostForm # Імпортуємо форму для створення постів
  from publications.models import Post,Image, Tag, Link # Імпортуємо моделі для роботи з публікаціями
  from .forms import PostForm, PostFormEdit # Імпортуємо форми для створення та редагування постів
  from settings_app.models import Profile, Friendship, Avatar # Імпортуємо моделі профілю, дружби та аватарів
  from django.urls import reverse_lazy # Імпортуємо функцію для отримання URL-адреси за назвою
  from django.contrib.auth.views import LogoutView # Імпортуємо клас для виходу з системи
  from django.shortcuts import redirect # Імпортуємо функцію для перенаправлення користувача на іншу сторінку
  from django.http import JsonResponse #Імпортуємо клас для створення JSON-відповідей
  from django.core import serializers # Імпортуємо модуль для серіалізації об'єктів
  from django.contrib.auth.models import User # Імпортуємо модель користувача
  from .forms import UserUpdateForm # Імпортуємо форму для оновлення користувача
  from chats.models import ChatGroup # Імпортуємо модель групи чату

  # Створюємо представлення для головної сторінки, де користувач може створювати та переглянути усі пости.
  class MainView(CreateView):
      template_name = "main/index.html" # Вказуємо шаблон для головної сторінки
      form_class = PostForm # Вказуємо форму для створення постів
      success_url = "/" # Вказуємо URL-адресу, куди буде перенаправлено користувача після успішного створення поста.
      # Створюємо метод, який буде викликано після валідації форми.
      def form_valid(self, form): 
          profile = Profile.objects.get(user_id=self.request.user.pk) # Отримуємо профіль поточного користувача.
          form.instance.author = profile # Присвоюємо автору поста профіль поточного користувача.
          response = super().form_valid(form) # Викликаємо метод батьківського класу для обробки валідної форми.
          urls = self.request.POST.getlist('url') # Отримуємо список URL-адрес з форми.
          for url in urls: # Якщо URL-адреси є, то створюємо об'єкт Link для кожної URL-адреси.
              url = Link.objects.create(post = self.object, url = url) # Отримуємо посилання, який пов'язаний з поточним постом.
          
          files = self.request.FILES.getlist('images') # Отримуємо список файлів з форми.
          for file in files: # Якщо файли є, то створюємо об'єкт Image для кожного файлу.
              image = Image.objects.create(filename = f"photo-{self.object}", file=file) # Створюємо об'єкт Image з файлом, який був завантажений.
              self.object.images.add(image) # Збираємо зображення до поста.
          return response # Повертаємо відповідь після успішного створення поста.
      
      # Створюємо метод, який буде викликано при обробці запиту.
      def dispatch(self, request, *args, **kwargs):
          if not Profile.objects.filter(user_id = request.user.id).exists(): # Якщо профіль користувача не існує.
              return redirect("registration") # То перенаправляємо на сторінку реєстрації
          current_user = Profile.objects.get(user_id = self.request.user.pk) # Отримуємо профіль поточного користувача.
          user_posts = Post.objects.all() # Отримуємо всі пости.
          if len(user_posts) > 0: # Перевіряємо, чи є пости.
              for post_view in user_posts: # Якщо пости є, то додаємо поточного користувача до переглядів кожного поста.
                  post_view.views.add(current_user) # Зберігаємо перегляд поста.
                  post_view.save() # Зберігаємо зміни в базі даних.
          return super().dispatch(request, *args, **kwargs) # Повертаємо відповідь у вигляді успадковування батьківського після обробки запиту.
      # Створюємо метод, який буде викликано для отримання контексту даних для шаблону.
      def get_context_data(self, **kwargs):
          context = super(MainView, self).get_context_data(**kwargs) # Успадковуємо контекст даних від батьківського класу.
          context["posts"] = Post.objects.all().order_by('-id') # Фільтруємо всі пости та сортуємо їх за спаданням ID(від більного до меншого).
          context["tags"] = Tag.objects.all() # Отримуємо всі теги.
          context['people'] = Profile.objects.get(user_id = self.request.user.pk) # Отримуємо профіль поточного користувача.
          context["all_urls"] = Link.objects.all() # Отримуємо всі URL-адреси.
          context['all_peoples'] = Profile.objects.all() # Отримуємо всі профілі користувачів.
          profile = Profile.objects.get(user_id = self.request.user.pk) # Отримуємо профіль поточного користувача.
          context["posts_count"] = Post.objects.filter(author_id = profile) # Отримуємо кількість постів, створених поточним користувачем.
          context["my_friends"] = Friendship.objects.filter(profile2 = profile, accepted = True) # Отримуємо список друзів поточного користувача, які підтвердили дружбу.
          context["all_requests"] = Friendship.objects.filter(profile2 = profile) # Отримуємо всі запити на дружбу, які надіслані поточному користувачу.
          context["all_users"] = Profile.objects.all() # Отримуємо всі профілі користувачів.
          author_avatars = {} # Створюємо словник для зберігання аватарів авторів.
          for author in Profile.objects.filter(id__in=Post.objects.values_list('author_id', flat=True)): # Перебираємо та проходимся по всім авторам постів.
              avatar = Avatar.objects.filter(profile=author, shown=True, active=True).first() # Отримуємо аватар автора, якщо він існує.
              author_avatars[author.id] = avatar # Додаємо аватар автора до словника author_avatars.
          for group in ChatGroup.objects.all(): # Перебираємо всі групи чату.
              for member in group.members.all(): # Проходимося по всім учасникам групи.
                  if member.id not in author_avatars: # Якщо аватар автора ще не додано до словника author_avatars.
                      avatar = Avatar.objects.filter(profile=member, shown=True, active=True).first() # Отримуємо аватар учасника групи, якщо він існує.
                      author_avatars[member.id] = avatar # Додаємо аватар учасника групи до словника author_avatars.
          for friend_ship in Friendship.objects.all(): # Перебираємо всі дружні зв'язки.
              if friend_ship.profile1 == Profile.objects.get(user_id = self.request.user.pk): # Якщо профіль 1 дружби дорівнює профілю поточного користувача.
                  if friend_ship.profile2.id not in author_avatars: # Якщо аватар профілю 2 дружби ще не додано до словника author_avatars.
                      avatar = Avatar.objects.filter(profile=friend_ship.profile2, shown=True, acive=True).first() # Створюємо аватар профілю 2 дружби, якщо він існує.
                      author_avatars[friend_ship.profile2.id] = avatar # Додаємо аватар профілю 2 дружби до словника author_avatars.
              if friend_ship.profile2 == Profile.objects.get(user_id = self.request.user.pk): #Якщо профіль 2 дружби дорівнює профілю поточного користувача.
                  if friend_ship.profile1.id not in author_avatars: # Якщо аватар профілю 1 дружби ще не додано до словника author_avatars.
                      avatar = Avatar.objects.filter(profile=friend_ship.profile1, shown=True, active=True).first() # Створюємо аватар профілю 1 дружби, якщо він існує.
                      author_avatars[friend_ship.profile1.id] = avatar # Додаємо аватар профілю 1 дружби до словника author_avatars.


          context['author_avatars'] = author_avatars # Передаємо словник author_avatars до контексту шаблону.
          context["my_avatars"] = Avatar.objects.filter(profile_id = profile.id) # Передаємо аватари поточного користувача до контексту шаблону.
          context['all_groups'] = ChatGroup.objects.all() # Передаємо всі групи чату до контексту шаблону.
          context["current_user"] = profile # Передаємо профіль поточного користувача до контексту шаблону.
          context['all_views'] = Post.objects.none() # Ініціалізуємо порожній QuerySet для зберігання всіх переглядів постів.
          for post in Post.objects.filter(author = profile): # Перебираємо всі пости, створені поточним користувачем.
              context['all_views'] = context['all_views'] | post.views.all() # Додаємо перегляди поста до загальних переглядів.
          return context # Повертаємо контекст даних для шаблону.
  # Створюємо представлення для видалення постів.  
  class MyDeleteView(DeleteView):
      template_name = "delete_post/index.html" # Вказуємо шаблон для сторінки видалення поста.
      model = Post # Вказуємо модель, з якою будемо працювати.
      success_url = reverse_lazy("main") # Вказуємо URL-адресу, куди буде перенаправлено користувача після успішного видалення поста.
  # Створюємо представлення для редагування постів.
  class EditView(UpdateView):
      model = Post # Вказуємо модель, з якою будемо працювати.
      form_class = PostFormEdit # Вказуємо форму для редагування постів.
      template_name = 'edit/edit_form.html' # Вказуємо шаблон для сторінки редагування поста.
      success_url = '/' # Вказуємо URL-адресу, куди буде перенаправлено користувача після успішного редагування поста.
      # Створюємо метод, який буде викликано після введення валідованих даних у форму.
      def form_valid(self, form):
          form.instance.user = self.request.user # Присвоюємо користувача, який редагує пост.
          # return super().form_valid(form) # Повертаємо відповідь після успішного редагування поста, успадковуючи метод батьківського класу.
  #Створюємо представлення для виходу з системи.
  class MyLogoutView(LogoutView):
      next_page = reverse_lazy('authorithation') # Вказуємо URL-адресу, куди буде перенаправлено користувача після виходу з системи.
  # Створюємо представлення для отримання даних поста.
  class PostDataView(View):
      # Створюємо представлення для отримання даних поста за його первинним ключем (post_pk).
      def post(self, request, post_pk):
          user_post = [Post.objects.get(pk = post_pk)] #Отримуємо пост за його первинним ключем.
          return JsonResponse(serializers.serialize("json", user_post), safe=False) # Повертаємо JSON-відповідь з даними поста.

  # Створюємо представлення для оновлення профілю користувача.
  class UserUpdateView( UpdateView):
      model = User # Ставимо модель користувача, яку будемо оновлювати.
      form_class = UserUpdateForm # вказуємо форму для оновлення користувача.
      template_name = 'main/index.html' # Вказуємо шаблон для сторінки оновлення користувача.
      success_url = reverse_lazy("main") #Вказуємо URL-адресу, куди буде перенаправлено користувача після успішного оновлення профілю.
  # Створюємо метод, який буде викликано для отримання об'єкта користувача, який буде оновлюватися.
      def get_object(self):
          return self.request.user # Повертаємо поточного користувача, який виконує запит.
      # Створюємо метод, який буде викликано після валідації форми.
      def form_valid(self, form):
          response = super().form_valid(form) # Викликаємо метод батьківського класу для обробки валідної форми.
          return response # Повертаємо відповідь після успішного оновлення профілю.
  # Створюємо представлення для отримання лайків поста.
  def get_likes(request,  post_pk):
      post = Post.objects.get(id = post_pk) # Отримуємо пост за його первинним ключем.

      profile = Profile.objects.get(user_id = request.user.id)  # Отримуємо профіль користувача.
      post.likes.add(profile) # Додаємо профіль користувача до лайків поста.
      post.save() # Зберігаємо зміни в пості.
      return redirect("/") # Перенаправляємо користувача на головну сторінку.

```

  ___

</details>

<details>
  <summary><strong>📁 publications</strong></summary>
  
  ___

  - Файл social_network/publications/views.py
    - views.py - файл для логіки додатку.

```python
  from django.contrib.auth.models import User # Імпортуємо модель User
  pubs/views
```

  ___


  - Файл social_network/publications/models.py
    - models.py - У файлі models.py ми визначаємо всі об'єкти, що називаються моделі - Models. Вона містить основні поля та поведінку даних, які ви зберігаєте.
  
```python
  from django.db import models # Імпортуємо models для роботи з моделями
  from settings_app.models import Profile # Імпортуємо модель профілю користувача

  # Створюємо модель поста, яка містить заголовок, контент, автора, зображення, перегляди, лайки, теги та тему.
  class Post(models.Model):
      title = models.CharField(max_length = 255)
      content = models.TextField(max_length = 4096)
      author = models.ForeignKey(Profile, on_delete = models.CASCADE, null = True, blank = True)
      images = models.ManyToManyField("Image", blank = True, related_name = "posts_authored")
      views = models.ManyToManyField(Profile, blank = True, related_name = "posts_viewed")
      likes = models.ManyToManyField(Profile, blank = True, related_name = "posts_liked")
      tags = models.ManyToManyField("Tag", blank = True)
      topic = models.CharField(max_length=255)

      def __str__(self):
          return self.title

  # Створюємо модель зображення, яка містить назву файлу, файл зображення та дату завантаження.
  class Image(models.Model):
      filename = models.CharField(max_length = 150)
      file = models.ImageField(upload_to = "images/posts")
      uploaded_at = models.DateTimeField(auto_now_add = True)
      
      def __str__(self):
          return self.filename

  # Створюємо модель альбому, яка містить назву, дату створення, зображення та тему.
  class Album(models.Model):
      name = models.CharField(max_length = 255)
      created_at = models.DateTimeField(auto_now_add = True)
      preview_image = models.ImageField(upload_to = 'images/album_previews',null = True, blank = True)
      images = models.ManyToManyField(Image,blank = True)
      shown = models.BooleanField(default=  True)
      topic = models.ForeignKey("Tag", on_delete=models.CASCADE)
      author = models.ForeignKey(Profile, on_delete = models.CASCADE)

      def __str__(self):
              return self.name
          
  # Створюємо модель тегу, яка містить назву тега.
  class Tag(models.Model):
      name = models.CharField(max_length = 50, unique = True)   
      def __str__(self):
          return self.name

  # Створюємо модель посилання, яка містить URL та пост, до якого воно належить.
  class Link(models.Model):
      url = models.URLField(max_length = 200)
      post = models.ForeignKey(Post, on_delete = models.CASCADE) 
      def __str__(self):
          return f'Посилання для поста "{self.post}"'
```

  ___

  - Файл social_network/publications/static/my_publications/script.js
    - script.js - js-файл для модальних вікон, завантаження картинок та аджаксу.
    
```javascript
    // Перебираємо усіх хрестиків для закриття модальних вікон
    for (let count = 0; count < crossesRedact.length; count++) {
        let crossRedact = crossesRedact[count]; // Знаходимо один об'єкт хрестика по індексу count
        let formRedact = formsRedact[count]; //  Знаходимо об'єкт форми по індексу
        // Створюємо прослуховувач для кожного хрестика по кліку
        crossRedact.addEventListener("click", () => {
            formRedact.classList.toggle("hidden"); // Змінюємо клас hidden: якщо клас hidden заданий - видаляємо. Якщо класа немає - задаємо
            bodyObject.classList.toggle("blur"); // Змінюємо клас blur: якщо клас blur заданий - видаляємо. Якщо класа немає - задаємо
        });
    }
    const input = document.querySelector("#image-to-post-form"); // Знаходимо input по його айді
    const previewDiv = document.querySelector("#image-preview-container"); // Знаходимо preview для картинок
    // Якщо input з preview існує
    if (input && previewDiv) {
        input.addEventListener("change", function () { // Створюємо прослуховувач по заданню картинок input
            previewDiv.innerHTML = ""; // Обнуляємо усі минулі картинки в input
            const files = Array.from(input.files); 
            // Перебираємо усі файли картинок в input. Кожен файл зберігається у змінній file
            files.forEach(file => { 
                // Перевіряємо, якщо тип файлу не починається на 'image/' - умова хибна
                if (!file.type.startsWith("image/")) return;
                const reader = new FileReader(); // Створюємо об'єкт для читання картинок
                // Загружаємо читача
                reader.onload = function (event) {
                    const img = document.createElement("img"); // Створюємо елемент зображення
                    img.src = event.target.result; // Отримуємо з читача результат та записуємо його до src зображення
                    img.classList.add("post-images-form") // Задаємо клас зображенню для дизайну
                    previewDiv.appendChild(img); // Записуємо елемент зображення до div-у
                };
                reader.readAsDataURL(file); // Записуємо результат читача як посилання
            });
        });
    };


```

  ___


</details>


<details>
  <summary><strong>📁 registration</strong></summary>

  - Файл social_network/registration/views.py
    - views.py - файл для логіки додатку.
   
  ---
  ```python
    from django.views.generic.edit import CreateView, FormView # Імпортуємо класи відображення для створення власних.
    from django.views.generic import TemplateView # Імпортуємо клас відображення для створення та рендерінгу власного.
    from django.urls import reverse_lazy # Імпортуємо reverse_lazy для надання зворотного URL як атрибут url загального відображення на основі класу.
    from .forms import VerificationForm, AuthorithationForm, RegistrationForm # Імпортуємо створені форми для валідації даних.
    from django.core.mail import send_mail # Імпортуємо функцію send_mail для відправки gmail-листа користувачеві.
    import random # Імпортуємо random для створення шестизначного коду.
    from django.contrib.auth.models import User # Імпортуємо модель User для створення користувача.
    from settings_app.models import Profile, VerificationCode # Імпортуємо створені моделі профілю та верифікації.
    from django.contrib.auth import authenticate, login # Імпортуємо функцію authenticate | login для аутентифікації та логіну користувача.
    from django.shortcuts import redirect #

    # Створюємо клас RegistrationView на базі вже створенного CreateView для відображення та логіки сторінки реєстрації.
    class RegistrationView(CreateView):
        form_class = RegistrationForm # Вказуємо форму для роботи з валідними даними.
        template_name = "registration/index.html" # Вказуємо файл html для відображення сторінки.
        success_url = reverse_lazy("confirm") # Вказуємо подію перекиду на сторінку верифікації після успішної реєстрації користувача.

        # Створюємо функцію post для .
        def post(self, request, *args, **kwargs):
            email = request.POST.get('email') # Отримуємо email, який користувач відправив у формі при реєстрації.
            if not User.objects.filter(email = email).exists(): # Якщо користувача з такою поштою ще нема.
                return super().post(request, *args, **kwargs) # Успадковуємо батьківський метод post, щоб продовжити стандартну обробку запиту.
            else:
                return redirect("registration") # Або перекидаємо користувача на сторінку реєстрації.
            
        # Створюємо метод form_valid, який відпрацює після того, як дані у формі будуть валідовані.
        def form_valid(self, form):
            response = super().form_valid(form) # Успадковуємо батьківський метод form_valid.
            response.set_cookie('email', form.cleaned_data['email'], max_age=3600) # Записуємо у cookie валідований email користувача на годину.
            special_code = random.randint(99999, 999999) # Створюємо рандомний шестизначний код для підтвердження особистості.
            # user_id = User.objects.get(email = form.cleaned_data['email']).id 
            user = form.save() # Зберігаємо у базу даних дані із форми.
            user.username = f"user-{user.pk}" # Додаємо вручну поле username з його id, яке є обов'язковим для бази даних і необов'язковим для реєстрації користувача.
            user.save() # Зберігаємо у базу даних створений username.
            Profile.objects.create(user = user) # Створюємо профіль на основі даних.
            VerificationCode.objects.create(username = user.username, code = special_code) # Створюємо та зберігаємо у базу даних шестизначний код.
            # Відправляємо email.
            send_mail(
                subject = "Код для підтвердження", # Заголовок листа.
                message = f"Вітаємо!\n ваш код для підтвердження: {special_code}", # Контент листа.
                from_email = "qrprojectdjangoteam2@gmail.com", # Email проєкту, від лиця якого надсилається лист.
                recipient_list = [f"{form.cleaned_data['email']}"], # Відправляємо на адресу користувача.
                fail_silently = False # Якщо в процесі відправки листа відбудеться помилка, показати її.
                )
            # Повертаємо response.
            return response
    # Створюємо клас ConfirmRegistrationView для відображення сторінки та логіки на сторінці confirm. 
    class ConfirmRegistrationView(FormView):
        template_name = "registration_confirm/index.html" # Вказуємо файл html для відображення сторінки.
        form_class = VerificationForm # Вказуємо форму для роботи з валідними даними.
        success_url = reverse_lazy("authorithation") # Вказуємо подію перекиду на сторінку аутентифікації після успішної реєстрації користувача.

        # Створюємо метод form_valid, який відпрацює після того, як дані у формі будуть валідовані.
        def form_valid(self, form):
            '''
                Отримуємо з форми маленькі валідовані інпути для введення даних.
            '''
            input1 = str(form.cleaned_data["input1"])
            input2 = str(form.cleaned_data["input2"])
            input3 = str(form.cleaned_data["input3"])
            input4 = str(form.cleaned_data["input4"])
            input5 = str(form.cleaned_data["input5"])
            input6 = str(form.cleaned_data["input6"])
            
            code_field = input1 + input2 + input3 + input4 + input5 + input6 # Створюємо код на основі інпутів. 
            email= self.request.COOKIES.get("email") # Отримуємо з cookie email користувача.
            username = User.objects.get(email = email).username # Отримуємо з бази даних користувача з email, на який було відправлено лист.
            user_code = VerificationCode.objects.get(username = username).code # Отримуємо з бази даних користувача з тільки-що надісланним кодом.
            
            if user_code == code_field: # Якщо код, який ввів користувач, правильний ш збігається з тим, що надісланий у листі.
                VerificationCode.objects.get(username = username).delete() # Видаляємо код з бази даних.
                return super().form_valid(form) # Повертаємо батьківський form_valid.
            else:
                form.add_error(None, "Код підтвердження не підходе!") # Якщо ні, виводити помилку.
                return self.form_invalid(form) # Форма не валідна.

    # Створюємо клас AuthorizationView для відображення сторінки та логіки на сторінці authorization. 
    class AuthorizationView(FormView):
        template_name="authorization/index.html" # Вказуємо файл html для відображення сторінки.
        form_class = AuthorithationForm # Вказуємо форму для роботи з валідними даними.
        success_url = "/" # Перекид на головну сторінку після успішної аутентифікації.

        # Створюємо метод form_valid, який відпрацює після того, як дані у формі будуть валідовані.
        def form_valid(self, form):
            email = form.cleaned_data['email'] # Отримуємо з форми введений email користувача.
            password = form.cleaned_data['password'] # Отримуємо з форми введений password користувача.
            # Перевіряємо, чи існує користувач з таким username та password.
            user = authenticate(username = email, password = password)
            # Якщо існує, то 
            if user is not None:
                login(self.request, user) # Логінемо користувача
                return super().form_valid(form) # Повертаємо батьківський form_valid.
            else:
                form.add_error(None, "Невірна пошта або пароль") # Якщо ні, виводити помилку.
                return self.form_invalid(form) # Форма не валідна.
  ```
  ---

  - Файл social_network/registration/forms.py
    - forms.py - файл для створення кастомних валідованих форм django.
  ___

  ```python 
      from django import forms # Імпортуємо модуль forms з django
      from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Імпортужмо UserCreationForm та AuthenticationForm з django.contrib.auth.forms
      from django.contrib.auth.models import User # Імпортуємо модель User з django.contrib.auth.models
      from settings_app.models import Profile # Імпортуємо модель Profile з settings_app.models


      # Створюємо форму для реєстрації, яка наслідує UserCreationForm для створення нового користувача
      class RegistrationForm(UserCreationForm):
          # Додаємо поле для введення електронної пошти
          email = forms.EmailField(max_length = 256,label = "Електронна пошта", widget = forms.EmailInput(attrs = {
                                                                              "placeholder": "you@example.com"
                                                                                    })) #
          # Додаємо поле для введення імені користувача
          password1 = forms.CharField(max_length= 12,label = "Пароль", widget = forms.PasswordInput(attrs = {
                                                                              "placeholder": "Введи пароль"
                                                                                      })) #
          # Додаємо поле для підтвердження пароля
          password2 = forms.CharField(max_length= 12,label = "Підтвердити", widget = forms.PasswordInput(attrs = {
                                                                              "placeholder": "Повтори пароль"
                                                                                      })) #
          # Створюємо мета-клас для вказання моделі та полів, які будуть використовуватись у формі
          class Meta:
              model = User # Вказуємо модель, з якою працюватиме форма
              fields = ["email"] # Вказуємо поля, які будуть включені у форму
              
      # Створюємо форму для авторизації, яка наслідує AuthenticationForm для входу користувача
      class AuthorithationForm(forms.Form):
          # Додаємо поле для введення імені користувача або електронної пошти
          email = forms.EmailField(max_length= 256,label = "Пошта", widget=forms.EmailInput(attrs ={
              "placeholder": "you@example.com" #
          })) 
          # Додаємо поле для введення пароля
          password = forms.CharField(widget = forms.PasswordInput(attrs = {
              "placeholder": "Введи пароль" #
          }), label = "Пароль") #


      # Створюємо форму для верифікації, яка наслідує forms.Form для збору шести полів вводу
      class VerificationForm(forms.Form):
          
          # Додаємо поле вводу 1 для верифікації
          input1 = forms.CharField(label = "", widget=forms.TextInput(attrs = { 
              "class": "input1 input", #
              "inputmode": "numeric" #
          })) 
          # Додаємо поле вводу 2 для верифікації
          input2 = forms.CharField(label = "", widget=forms.TextInput(attrs = { #
              "class": "input2 input" #
          })) 
          # Додаємо поле вводу 3 для верифікації
          input3 = forms.CharField(label = "", widget=forms.TextInput(attrs = { # 
              "class": "input3 input" #
          }))
          # Додаємо поле вводу 4 для верифікації
          input4 = forms.CharField(label = "", widget=forms.TextInput(attrs = { #
              "class": "input4 input" #
          })) 
          
          # Додаємо поле вводу 5 для верифікації
          input5 = forms.CharField(label = "", widget=forms.TextInput(attrs = { #
              "class": "input5 input" # 
          })) 
          
          # Додаємо поле вводу 6 для верифікації
          input6 = forms.CharField(label = "", widget=forms.TextInput(attrs = { #
              "class": "input6 input" #
          })) 
          
          
  ```
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

</details>


<details>
  <summary><strong>📁 settings_app</strong></summary>

  ___
  - Файл social_network/settings_app/models.py
    - models.py -  У файлі models.py ми визначаємо всі об'єкти, що називаються моделі - Models. Вона містить основні поля та поведінку даних, які ви зберігаєте.
```python
  from django.db import models # Імпортуємо models для роботи з моделями
  from django.contrib.auth.models import User # Імпортуємо модель користувача
  from django.contrib.auth import get_user_model # Імпортуємо функцію для отримання користувача
  from django.conf import settings # Імпортуємо налаштування проекту

  # Створюємо модель профілю користувача, яка розширює модель User та міститиме додаткову інформацію - дату народження та підпис.
  class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      date_of_birth = models.DateField(null = True)   
      signature = models.ImageField(upload_to="images/signatures", blank = True, null = True)

      def __str__(self):
          return self.user.username

  # Створюємо модель аватара користувача яка містититьв собі зображення аватара, пов'язане з профілем користувача, активність/прихованість його аватарок.
  class Avatar(models.Model):
      image = models.ImageField(upload_to = "images/avatars")
      profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
      active = models.BooleanField(default = True)
      shown = models.BooleanField(default = True)
      def __str__(self):
          return f'Аватар для профілю {self.profile}'

  # Створюємо модель дружби, яка міститиме інформацію про профілі користувачів, які стали друзями, та статус дружби (прийнято чи ні).
  class Friendship(models.Model):
      profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friendship_sent_request") # Той, хто надсилає запит
      profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friendship_accepted_request") # Той, хто приймає запит
      accepted = models.BooleanField(default=False)

      def __str__(self):
          return f'Дружба між {self.profile1} та {self.profile2}'

  # Створюємо модель VerificationCode, яка міститиме інформацію про код підтвердження, пов'язаний з користувачем, та дату його створення.
  class VerificationCode(models.Model):
      username = models.CharField(max_length=150)
      code = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add=True)

```
___
  
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
