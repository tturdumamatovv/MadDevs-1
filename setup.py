from setuptools import setup, find_packages  # Импортируем функции setup и find_packages из setuptools

setup(
    name="migrations",  # Указываем имя пакета
    version="1.0",  # Указываем версию пакета
    packages=find_packages(),  # Находим и указываем все пакеты в проекте
) 