# TeamFinder

Платформа для поиска участников в командные IT-проекты.

## Описание

TeamFinder — веб-приложение, которое позволяет пользователям создавать проекты, искать участников для совместной работы, а также вступать в уже существующие проекты. Реализованы функции добавления проектов в избранное, отметки проекта как завершённого, авторизации пользователей и управления профилем.

## Стек технологий

- Python 3.x
- Django 4.x
- PostgreSQL
- Docker / Docker Compose
- HTML / CSS (шаблоны Django)

## Развёртывание проекта

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/vrudakov1315-art/practicum_yandex_2.git
cd practicum_yandex_2
```

### 2. Создайте файл `.env` на основе `.env.example`

```bash
cp .env.example .env
```

Заполните `.env` своими значениями (см. раздел ниже).

### 3. Запустите через Docker Compose

```bash
docker compose up --build
```

### 4. Примените миграции

```bash
docker compose exec web python manage.py migrate
```

### 5. Создайте суперпользователя (опционально)

```bash
docker compose exec web python manage.py createsuperuser
```

Приложение будет доступно по адресу: http://localhost:8000

## Переменные окружения (`.env`)

| Переменная | Описание | Пример |
|---|---|---|
| `DJANGO_SECRET_KEY` | Секретный ключ Django | `any-random-string-here-12345` |
| `DJANGO_DEBUG` | Режим отладки | `True` |
| `ALLOWED_HOSTS` | Разрешённые хосты | `localhost,127.0.0.1` |
| `POSTGRES_DB` | Имя базы данных | `team_finder` |
| `POSTGRES_USER` | Пользователь БД | `team_finder` |
| `POSTGRES_PASSWORD` | Пароль БД | `team_finder` |
| `POSTGRES_HOST` | Хост БД | `db` |
| `POSTGRES_PORT` | Порт БД | `5432` |

## Автор

- GitHub: [vrudakov1315-art](https://github.com/vrudakov1315-art)
