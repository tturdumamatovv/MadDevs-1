# Start of Selection
# Используем образ Python версии 3.10
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt без кэширования
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . /app/

# Устанавливаем текущее приложение в режиме редактирования
RUN pip install -e .

# Меняем рабочую директорию на /app/code
WORKDIR /app/code

# Копируем скрипт entrypoint в корневую директорию контейнера
COPY docker/entrypoint.sh /entrypoint.sh

# Делаем скрипт entrypoint исполняемым
RUN chmod +x /entrypoint.sh

# Установка netcat для проверки доступности сервисов
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Устанавливаем скрипт entrypoint как точку входа для контейнера
ENTRYPOINT ["/entrypoint.sh"] 
