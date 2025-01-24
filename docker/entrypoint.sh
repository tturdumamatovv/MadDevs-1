#!/bin/bash

# Ожидание доступности PostgreSQL
echo "Waiting for PostgreSQL..."  # Выводим сообщение о начале ожидания
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do  # Проверяем доступность PostgreSQL по указанному хосту и порту
  sleep 0.1  # Ждем 0.1 секунды перед следующей проверкой
done
echo "PostgreSQL started"  # Выводим сообщение о том, что PostgreSQL доступен

# Применение миграций
python manage.py migrate  # Выполняем миграции базы данных для применения изменений

# Загрузка тестовых данных
python manage.py load_test_data  # Загружаем тестовые данные в базу данных

# Запуск сервера
python manage.py runserver 0.0.0.0:8000  # Запускаем сервер Django, доступный на всех интерфейсах по порту 8000