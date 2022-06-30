import json

from main.functions import load_all_posts


def add_post(post: dict):
    """
    Добавляет пост в файл
    :param post:
    :return:
    """
    posts: list[dict] = load_all_posts()
    posts.append(post)
    with open('posts1.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post


def save_picture(img):
    """
    Производит сохранение картинки на локальный пк
    :param img:
    :return:
    """
    filename = img.filename
    file_storage = f"./uploads/images/{filename}"
    img.save(file_storage)
    return file_storage
