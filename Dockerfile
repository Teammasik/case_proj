# Используем официальный образ Python, поддерживающий работу с ARM
FROM python:3.8-slim-buster

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Обновляем список пакетов и устанавливаем необходимые зависимости для сборки psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev

# Копируем файл requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы и директории в рабочую директорию
COPY . .

# Экспортируем переменные окружения
ENV DATABASE_URL=postgresql://admin:password@localhost/database
ENV DATABASE_URL_ASYNC=postgresql+asyncpg://admin:password@localhost/database

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]