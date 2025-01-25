.PHONY: up down build logs build-d up-d test coverage coverage-report coverage-html

up:  # Запуск контейнеров
	docker-compose --env-file .env -f docker/docker-compose.yml up

build:  # Сборка и запуск контейнеров
	docker-compose --env-file .env -f docker/docker-compose.yml up --build

up-d:  # Запуск контейнеров в фоновом режиме
	docker-compose --env-file .env -f docker/docker-compose.yml up -d

build-d:  # Сборка и запуск контейнеров в фоновом режиме
	docker-compose --env-file .env -f docker/docker-compose.yml up -d --build

down:  # Остановка контейнеров
	docker-compose -f docker/docker-compose.yml down

logs:  # Просмотр логов контейнеров
	docker-compose -f docker/docker-compose.yml logs -f

# Команды для тестирования
test:  # Запуск тестов
	docker-compose -f docker/docker-compose.yml exec web python manage.py test ../tests/patients/

coverage:  # Запуск тестов с покрытием
	docker-compose -f docker/docker-compose.yml exec web coverage run manage.py test ../tests/patients/

coverage-report:  # Отчет о покрытии
	docker-compose -f docker/docker-compose.yml exec web coverage report

coverage-html:  # Создание HTML отчета о покрытии
	docker-compose -f docker/docker-compose.yml exec web coverage html 