![foodgram workflow](https://github.com/Sergey-Aleksandrovich/foodgram-project/workflows/foodgram%20workflow/badge.svg)
# Название проекта

Foodgram - это проект, в котором возможно добавлять понравившиеся рецепты в покупки и получать список с необходимыми ингредиентами.

## Ссылка на пример проекта в интернете

### [Проект Foodgram](https://test-recipes.tk/?breakfast=True&lunch=True&dinner=True)

Чтобы увидеть весь функционал рекомендую зарегестрироваться или воспользоваться тестовым аккаунтом.

Логин: test 

Пароль: Test1231230

## Описание проекта

Проект Foodgram - это продуктовый помощник 

* Возможности проекта: 

    проект, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
    
* Цель проекта:

    Продемонстрировать наиболее наглядно навыки backend-разбаробчика, с использованием фреймворка Django.
    
* Используемые [технологии](https://test-recipes.tk/about/tech/):

   - GitHub
   - DRF
   - Django
   - PostgreSQL
   - Nginx
   - Gunicorn
   - Docker
   - HTML 5 (Редактирование готовых шаблонов и создание простых. Пример: [о авторе](https://test-recipes.tk/about/author/))

## Быстрый старт

Эти инструкции позволят вам запустить копию проекта на вашем компьютере.

### Скачавание и запуск проекта

Скачайте данный проект на свой ПК

Установите необходимые настройки nginx, postgreSQL, django в файлах db.env, django.env, nginx.env.

Желательно получить сертификат SSL c помощью certbot.

Команда для запуска проекта
 
```
docker-compose up
```

### Выполнение миграций

```
docker-compose exec web python manage.py migrate
```

### Заполнение базы начальными данными

Команда для заполнения базы начальными данными

```
docker-compose exec web python manage.py loaddata fixtures.json
```

### Сбор статики

```
docker-compose exec web python manage.py collectstatic
```

