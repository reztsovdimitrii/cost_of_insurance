# Cервис по расчёту стоимости страхования

- [ ] [Описание](#описание)
- [ ] [Технологии](#технологии)
- [ ] [Начало работы](#начало-работы)
- [ ] [Зависимости](#зависимости)
- [ ] [Установка](#установка)
- [ ] [Использование API сервиса до развертки](#использование-api-сервиса-до-развертки)
- [ ] [Работа с Docker](#работа-с-docker)
 

### Описание
Сервис по расчёту стоимости страхования реализован на асинхронном фреймворке FastAPI.
API полностью дают возможность реализовать полноценный web-сервис для расчета страхования  в зависимости от типа груза и объявленной стоимости (ОС).
Тариф может загружаться из файла JSON или принимать подобную JSON структуру:
```json
    {
	    "2020-06-01": [
		    {
			    "cargo_type": "Glass",
			    "rate": "0.04"
			},
			{
				"cargo_type": "Other",
				"rate": "0.01"
			}
		],
		"2020-07-01": [
			{
				"cargo_type": "Glass",
				"rate": "0.035"
			},
			{
				"cargo_type": "Other",
				"rate": "0.015"
			}
		]
	}
```

### Технологии
[![Python][Python-badge]][Python-url] [![FastAPI][FastAPI-badge]][FastAPI-url] [![PostgreSQL][PostgreSQL-badge]][PostgreSQL-url] [![Docker][Docker-badge]][Docker-url] 

### Начало работы

Чтобы запустить локальную копию сервиса, следуй инструкциям ниже.

### Зависимости

- [Python 3.7+][Python-url]

### Установка

1. **Клонировать репозиторий**

    ```bash
    git clone git@github.com:reztsovdimitrii/cost_of_insurance.git
    ```
2. **Создать, активировать виртуальное окружение**
	```bash
    python -m venv venv
    ```
3. **Установить зависимости проекта**
    ```bash
    pip install -r requirements.txt
    ```
4. **Создание базы данных и переменного окружения**
	Сервис использует базу данных PostgreSQL, поэтому нужно установить себе на локальный сервер.  
	Для подключения и выполнения запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в корневой папке сервиса.

	Шаблон для заполнения файла ".env":
	```python
	DATABASE_CONNECTION_URL=postgres://postgres:password@localhost:5432/postgres # ссылка на подключение к вашей БД
	```
5.  **Создать базу данных и выполнить миграции**
	В терминале bash корневой директории сервиса cost_of_insurance  запустить команду для миграции базы данных. Перед этим убедится, что ваша БД развернута и активна.
	```bash
	aerich upgrade
	```
6. **Запуск API сервиса для бронирования переговорных**
	Запустить сервис можно в терминале bash командой:
	```bash
	uvicorn app.main:app --reload
	```
	Доступ к API сервиса можно проверить по адресу [http://localhost/docs](http://localhost:8000/docs) будет запущена открытая документация API формата Swagger, где вы можете выполнить запросы на эндпоинты.

### Использование API сервиса до развертки
В корневой директории проекта находится redoc.json с помощью сервиса [Redocly](https://redocly.github.io/redoc/) можно прочитать как устроен данный API до запуска сервиса на локальном сервере. Если вас устроит данный web-сервис буду рад помочь =)

### Работа с Docker
В корневой директории проекта находится Dockerfile и docker-compose.yml, чтобы развернуть сервис с помощью docker контейнеров нужно выполнить:

1.  **Создать образ**
    ```bash
    sudo docker-compose build
    ```
2.  **Запустить сервис**
    ```bash
    sudo docker-compose up
    ```
3.  **Работа с сервисом**
	После запуска docker-compose  web-сервис будет разворачивать по адресу указанному в docker-compose.yml, а именно [http://0.0.0.0:8000](http://0.0.0.0:8000). Чтобы проверить работу API через Swagger  можно перейти по этому адресу  [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs).
5. **Закончить работу сервиса**
	```bash
    sudo docker-compose down
    ```
---

<h4 align="center">
Автор сервиса: <a href="https://github.com/reztsovdimitrii">Дмитрий Резцов</a>
</h4>

<!-- MARKDOWN BADGES & URLs -->

[Python-url]: https://www.python.org/
[Python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[FastAPI-url]: https://fastapi.tiangolo.com/
[FastAPI-badge]: https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
[PostgreSQL-badge]: https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white
[Docker-url]: https://www.docker.com/
[Docker-badge]: https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white
