# Patients API

API сервис для управления пациентами с JWT-авторизацией и разделением ролей (doctor/patient).

## Запуск проекта

1. Перейдите в директорию `docker`:
```bash
cd docker
```

2. Запустите проект с помощью Docker Compose:
```bash
docker-compose up -d --build 
```

**Важно**: Проект нужно запускать именно из директории `docker`, запуск из корневой директории работать не будет.

**Примечание**: При запуске контейнера автоматически выполняются следующие действия:
- Применение миграций (`python manage.py migrate`)
- Загрузка тестовых данных (`python manage.py load_test_data`)
- Запуск сервера

## Структура репозитория

1. `tests/` - Тесты проекта
   - `patients/` - Тесты для приложения patients
     - `test_models.py` - Тесты моделей
     - `test_admin.py` - Тесты админ-панели
     - `test_permissions.py` - Тесты прав доступа
     - `test_commands.py` - Тесты команд

2. `code/` - Исходный код проекта
   - `core/` - Основные настройки Django
   - `patients/` - Приложение для работы с пациентами
     - `models.py` - Модели User и Patient
     - `views.py` - API endpoints
     - `permissions.py` - Права доступа
     - `serializers.py` - Сериализаторы для API

3. `docker/` - Docker конфигурация
   - `Dockerfile` - Сборка приложения
   - `docker-compose.yml` - Оркестрация контейнеров
   - `entrypoint.sh` - Скрипт инициализации

4. `migrations/` - Миграции базы данных
   - `patients/` - Миграции для моделей пациентов
   - `admin/` - Миграции для админки
   - и другие системные миграции

## Быстрый старт

### Предварительные требования

- Docker
- Docker Compose

### Запуск проекта

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Создайте файл .env в корне проекта:
```env
DEBUG=True
ALLOWED_HOSTS=*
DB_NAME=maddevs
DB_USER=hello
DB_PASSWORD=1
DB_HOST=db
DB_PORT=5432
POSTGRES_HOST_AUTH_METHOD=trust
SITE_ID=1
SECRET_KEY='django-insecure-#9&!9g3d8cg7fvk_x-_58$qy!-66@su+$oaeuj3(x=1j_p(20r'
```

3. Запустите проект через Docker Compose:
```bash
docker-compose up -d --build
```

# Тестовые данные создаются автоматически при запуске контейнера

### Тестовые пользователи

1. Администратор:
   - username: admin
   - password: admin123
   - role: doctor

2. Доктор:
   - username: doctor
   - password: doctor123
   - role: doctor

3. Пациент:
   - username: patient
   - password: patient123
   - role: patient

## API Endpoints

### 1. Авторизация

```http
POST /login/

{
    "username": "doctor",
    "password": "doctor123"
}
```

Ответ:
```json
{
    "access": "your.jwt.token",
    "refresh": "your.refresh.token"
}
```

### 2. Список пациентов (только для докторов)

```http
GET /patients/
Authorization: Bearer your.jwt.token
```

Ответ:
```json
[
    {
        "id": 1,
        "date_of_birth": "1990-05-15",
        "diagnoses": ["Грипп", "ОРВИ"],
        "created_at": "2024-01-24T10:30:00Z"
    }
]
```

## Разработка

### Запуск тестов

```bash
# Запуск тестов в Docker
docker compose exec web python manage.py test ../tests/patients/
```

### Проверка покрытия кода

```bash
# Запуск coverage в Docker
docker compose exec web coverage run manage.py test ../tests/patients/
docker compose exec web coverage report
docker compose exec web coverage html  # создает HTML отчет в htmlcov/
```

HTML отчет о покрытии будет доступен в `htmlcov/index.html`

## Административная панель

Доступна по адресу: http://localhost:8000/admin/
- Используйте учетные данные администратора для входа
- Управление пользователями и пациентами

## Документация API

Swagger UI доступен по адресу: http://localhost:8000/api/docs/

## Технологии

- Python 3.8+
- Django 5.0.2
- Django REST Framework
- PostgreSQL
- Docker
- JWT Authentication