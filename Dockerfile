# Используем официальный легковесный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Обновляем pip и устанавливаем системные зависимости, необходимые для некоторых Python-библиотек
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Обновляем pip до последней версии
RUN pip install --upgrade pip

# Копируем только файл зависимостей, чтобы использовать кеш
COPY requirements.txt .

# Устанавливаем зависимости без сохранения кэша
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .