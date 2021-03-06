from flask import Flask, request, render_template, send_from_directory
# from functions import get_by_word
import logging
# Импортируем блюпринты из их пакетов
from main.views import main_blueprint
from loader.views import new_post_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрируем блюпринт c указание префикса
app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(new_post_blueprint)

# Добавили файл, в который пишем логи
logging.basicConfig(filename="basic.log", level=logging.INFO)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(host='0.0.0.0', port=80)
