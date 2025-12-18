from flask import Flask

# Создаем объект приложения Flask
app = Flask(__name__)

# Импортируем маршруты
from app import routes