import logging
from json import JSONDecodeError

from flask import render_template, Blueprint, request

from loader.functions import save_picture, add_post

new_post_blueprint = Blueprint('new_post_blueprint', __name__, template_folder='templates')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@new_post_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html',)


@new_post_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    img = request.files.get('picture')
    text = request.form.get('content')
    if not img or not text:
        return "Ошибка загрузки. Нет картинки или текста"
    if img.filename.split(".")[-1] not in ALLOWED_EXTENSIONS:
        logging.info('This is not a jpg or png')
        return 'Неправильное расширение.'
    try:
        picture_path: str = '/' + save_picture(img)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    new_post = add_post({'pic':picture_path, 'content':text})
    return render_template('post_uploaded.html',
                            post=new_post)




