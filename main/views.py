from json import JSONDecodeError
import logging
from flask import render_template, Blueprint, request

from main.functions import get_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_name = request.args.get('s', '')
    logging.info('Doing some research...')
    try:
        post = get_by_word(search_name)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html',
                           search_name=search_name,
                           posts=post)
