from flask import request, jsonify
from app import app
from datetime import datetime

# Главная страница — приветствие
@app.route('/')
def index():
    return "Привет! Это простейший веб-сервис на Flask."

# Персональное приветствие
@app.route('/hello/<name>')
def hello(name):
    return f"Привет, {name}!"

# Квадрат числа
@app.route('/square/<int:number>')
def square(number):
    return f"Квадрат числа {number} равен {number ** 2}"

# Вариант 1: сумма двух чисел через query-параметры
@app.route('/sum')
def sum_numbers():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return "Ошибка: нужно передать параметры a и b", 400
    return f"Сумма {a} + {b} = {a + b}"

# Вариант 1: информация о сервисе
@app.route('/info')
def info():
    info_data = {
        "version": "1.0",
        "author": "Тая Полковникова",
        "start_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(info_data)