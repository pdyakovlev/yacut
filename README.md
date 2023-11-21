# YaCut

## Описание

Сервис укорачивания ссылок – заменяет длинную ссылку на компактную (6 - 16 символов).  
Вариант сокращение может задан как самим пользователем, так и сгенерирован автоматически сервисом.  
Все сокращения уникальны. Реализован **web**-интерфейс и **REST API**.

## Оглавление

- [Технологии](#технологии)
- <a href="#t1"> Структура проекта </a>
- [Запуск](#запуск)
- [Автор](#автор)

## Технологии

- Python
- Flask
- Flask-SQLAlchemy

<details>
  <summary>
    <h2 id="t1"> Структура проекта </h2>
  </summary>

  ```cmd
  yacut:
  |   .env.dist  <-- Конфигурационные данные
  |   .flake8
  |   .gitignore
  |   openapi.yml  <-- Документация по API
  |   pytest.ini
  |   README.md
  |   requirements.txt
  |   settings.py  <-- Настройки сервиса
  |
  +---tests  <-- Тесты (pytest в корне дир., в консоли)
  |   |
  |   \---__pycache__
  |           
  +---venv  <-- Виртуальное окружение
  |
  +---yacut
  |   |   api_views.py  <-- Методы для API
  |   |   constants.py  <-- Константные переменные
  |   |   error_handlers.py  <-- Обработчик ошибок
  |   |   exceptions.py  <-- Кастомные исключения
  |   |   forms.py  <-- Форма для пользователя
  |   |   models.py  <-- Модель БД
  |   |   utils.py  <-- Функция, генерирующая уникальное сокращение
  |   |   views.py  <-- Методы для web
  |   |   __init__.py
  |   |   
  |   +---static  <-- Статика
  |   |
  |   +---templates  <-- HTML-шаблоны
  |   |           
  |   \---__pycache__
  |
  \---__pycache__
  ```

</details>

[⬆️Оглавление](#оглавление)

## Установка

- Cоздать и активировать виртуальное окружение:
  ```python
  python3 -m venv venv
  (win) source venv/Scripts/activate
  (linux) source venv/bin/activate
  ```

- Установить зависимости:
  ```python
  pip install -r requirements.txt
  ```

- Выполнить миграции:
  ```python
  flask db init
  flask db migrate -m "<сообщение>"
  flask db upgrade
  ```

- Запустить в терминале командой:
  ```python
  flask run
  ```
  [⬆️Оглавление](#оглавление)