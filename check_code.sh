#!/bin/bash

# Проверяем, передан ли файл
if [ -z "$1" ]; then
    echo "Использование: $0 <путь_к_файлу>"
    exit 1
fi

FILE=$1

# Проверяем, существует ли файл
if [ ! -f "$FILE" ]; then
    echo "Ошибка: файл '$FILE' не найден!"
    exit 1
fi

# Запускаем команды
echo "Запускаем isort..."
isort "$FILE"

echo "Запускаем black..."
black -l 120 "$FILE"

echo "Запускаем mypy..."
mypy "$FILE"

echo "Запускаем pylint..."
pylint "$FILE"

echo "Все проверки завершены!"
