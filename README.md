[//]: # (Бот-парсер API с сайта https://rapidapi.com/apidojo/api/hotels4/)

[//]: # ()
[//]: # (Для использования скрипта необходимо зарегистрироваться на сайте rapidapi и оформить подписку на отправку запросов &#40;)

[//]: # (базовая бесплатна, 500 запросов&#41;)

[//]: # ()
[//]: # (Создать бота у BotFather)

[//]: # ()
[//]: # (Создать файл .env, где прописать данные из env.template)

[//]: # ()
[//]: # (В качестве БД для получения истории запросов используется PostgreSQL, gino; для взаимодействия с API сайта aiohttp;)

[//]: # (функционал бота aiogram)

[//]: # ()
[//]: # (Бот по команде /low производит поиск самых недорогих отелей в локации прописанной пользователем, /high - самые дорогие,)

[//]: # (/bestdeal - поиск по введённым пользователем диапазоном цен и расстояние до центра города &#40;до 10 отелей&#41;)

[//]: # ()
[//]: # (/history - последние запросы пользователя с информацией о введенной команде, датой и временем введенной команды и)

[//]: # (найденными отелями)

-Создать бота у BotFather
-Создать файл .env, где прописать данные из env.template
-Создаём шаблон с папками

Папки:
-config_data - происходит инициализация (бота, БД, диспетчера)
-database - создаём структуру базы данных
-handlers - создаём обработчики(функции), цепляем к роутерам, импортируем их в файле __init__, затем в файле bot.py 
регистрируем роутеры.
-keyboards - создаём клавиатуры, которые пользователю будут показаны в ТГ боте
-states - 
-static - содержит статические файлы(фото, видео)
-utils - 
-lexicon - содержит словарь с данными, которые будут показаны пользователю.
Файл bot.py - предназначен для запуска бота 
     loader.py - инициализируем переменные для импорта
     requirements.txt - файл с библиотеками и их версиями, которые использовались при написании бота. 
