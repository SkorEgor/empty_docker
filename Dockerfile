# Базовый образ
FROM python:3.10-slim

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt requirements.txt

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения
COPY app app
COPY .env .env