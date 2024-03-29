# Тестовое задание

### Запуск проекта

```
docker-compose up --build
docker-compose exec backend python manage.py migrate
```

### Тестирование

```
docker-compose exec backend python manage.py test
```

Общее.

Азиз – имеет свой бизнес. Занимается продажей медтехники. У него много сотрудников и он как хороший босс хочет поощрять своих лучших сотрудников. А также он хочет наблюдать кто как работает (посмотреть статистику). Сейчас он считает все вручную.

В статистику сотрудника должны войти:

* Количество проданных товаров
* Количество уникальных клиентов
* Общая сумма продаж** **

Статистика нужно вывезти на определенный период

В статистику клиента должны войти:

* Количество купленных товаров
* Общая сумма продаж** **

Ваша задача реализовать REST API на DRF, которое может

* Посчитать статистику отдельного сотрудника
* Посчитать статистику всех сотрудников
* Посчитать статистику отдельного клиента

Требования:

* DRF (Django Rest Framework),
* Docker
* База данных на усмотрение (рекомендуем**  **Postgres)

Задачу нужно сделать в течении 3 дней со дня получения. Ответом отправьте ссылку на гитхаб репозиторий.

Техническое задание.

- метод **get** **** ** *** /statistics/employee/{id}/?month=1&year=2023*

возвращает *– ФИО, количество клиентов, количество товаров, сумму продаж*

** **- метод **get** **  ***/employee/statistics/?month=1&year=2023*

возвращает *– id сотрудника, ФИО, количество клиентов, количество товаров, сумму продаж*

- метод **get**   * /statistics/client/{id}?month=1&year=2023*

возвращает *– id клиента, ФИО, количество купленных товаров, сумму продаж*

Сущности для использования.

Employee(сотрудник):

**   ****full_name** – ФИО

**   ****birthdate** – дата рождения

Client(клиент)

**   ****full_name** - ФИО**	**

**   ****birthdate** – дата рождения

Product (продукт):

**   ****name** - имя продукта

**   ****quantity** - количество в наличии

**   ****price** - цена

Order(заказ):

**    ****client** – клиент

**    ****products** – продукты (может быть несколько товаров в заказе)

**    ****employee** – сотрудник

**    ****price** – общая цена заказа

**    ****date** - дата заказа
