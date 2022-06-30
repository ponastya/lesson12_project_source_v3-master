import json

from main.functions import load_all_posts


def add_post(post: dict) -> dict:
    posts: list[dict] = load_all_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post



ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def save_picture(img):
    filename = img.filename
    if filename.split(".")[-1] not in ALLOWED_EXTENSIONS:
        return 'Неправильное расширение.'
    file_storage = f"./uploads/images/{filename}"
    img.save(file_storage)
    return file_storage
