# Patients API

API сервис для управления пациентами с JWT-авторизацией и разделением ролей (doctor/patient).

## Быстрый старт

### Предварительные требования

- Docker
- Docker Compose

### Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone git@github.com:tturdumamatovv/MadDevs-1.git
cd MadDevs-1
```

2. Создайте файл `.env` в корневой директории проекта:
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

3. Перейдите в директорию `docker`:
```bash
cd docker
```

4. Запустите проект:
```bash
docker-compose up -d --build
```

**Важно**: Проект нужно запускать именно из директории `docker`

### Доступ к сервисам

- API: http://localhost:8000/
- Админ-панель: http://localhost:8000/admin/
- API документация (Swagger): http://localhost:8000/api/docs/

## Тестовые пользователи

| Роль          | Логин    | Пароль    |
|---------------|----------|-----------|
| Администратор | admin    | admin123  |
| Доктор        | doctor   | doctor123 |
| Пациент       | patient  | patient123|

## API Endpoints

### Авторизация

```http
POST /login/
Content-Type: application/json

{
    "username": "doctor",
    "password": "doctor123"
}
```

### Список пациентов (только для докторов)

```http
GET /patients/
Authorization: Bearer your.jwt.token
```

## Разработка

### Запуск тестов
```bash
docker-compose exec web python manage.py test ../tests/patients/
```

### Проверка покрытия кода
```bash
# Запуск тестов с coverage
docker-compose exec web coverage run manage.py test ../tests/patients/

# Просмотр отчета
docker-compose exec web coverage report

# Создание HTML отчета
docker-compose exec web coverage html
```

## Структура проекта

```
.
├── code/                  # Исходный код
│   ├── core/             # Настройки Django
│   └── patients/         # Приложение для работы с пациентами
├── docker/               # Docker конфигурация
├── migrations/           # Миграции БД
└── tests/               # Тесты
```

## Технологии

- Python 3.8+
- Django 5.0.2
- Django REST Framework
- PostgreSQL
- Docker
- JWT Authentication
