# TeamFinder

## Описание проекта

TeamFinder — платформа для разработчиков, дизайнеров и других специалистов, которые хотят находить единомышленников для совместной работы над pet-проектами. Зарегистрированные пользователи могут публиковать идеи проектов, находить команду и откликаться на опубликованные предложения.

## Стек технологий

- **Python 3.11+**
- **Django 4.x** — backend-фреймворк
- **PostgreSQL** — база данных
- **Pillow** — генерация аватаров
- **python-decouple** — управление переменными окружения
- **Docker / Docker Compose** — контейнеризация
- **HTML / CSS / JavaScript** — фронтенд (шаблоны Django)

## Инструкция по развертыванию

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/vrudakov1315-art/practicum_yandex_2.git
cd practicum_yandex_2
```

### 2. Создайте файл `.env` на основе примера

```bash
cp .env.example .env
```

Отредактируйте `.env`, указав свои значения (см. раздел «Переменные окружения»).

### 3. Запустите проект через Docker Compose

```bash
docker-compose up --build
```

### 4. Примените миграции

```bash
docker-compose exec web python manage.py migrate
```

### 5. Создайте суперпользователя (опционально)

```bash
docker-compose exec web python manage.py createsuperuser
```

Проект будет доступен по адресу: `http://localhost:8000`

## Переменные окружения

| Переменная | Описание | Пример |
|---|---|---|
| `DJANGO_SECRET_KEY` | Секретный ключ Django | `your-secret-key` |
| `DJANGO_DEBUG` | Режим отладки | `True` / `False` |
| `ALLOWED_HOSTS` | Список разрешённых хостов | `localhost,127.0.0.1` |
| `POSTGRES_DB` | Имя базы данных | `team_finder` |
| `POSTGRES_USER` | Пользователь БД | `team_finder` |
| `POSTGRES_PASSWORD` | Пароль БД | `team_finder` |
| `POSTGRES_HOST` | Хост БД | `db` |
| `POSTGRES_PORT` | Порт БД | `5432` |

## Контакты

Автор: [vrudakov1315-art](https://github.com/vrudakov1315-art)
