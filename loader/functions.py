import json

from main.functions import load_all_posts


def add_post(post: dict) :
    posts: list[dict] = load_all_posts()
    posts.append(post)
    with open('posts1.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post





def save_picture(img):
    filename = img.filename


    file_storage = f"./uploads/images/{filename}"
    img.save(file_storage)
    return file_storage
