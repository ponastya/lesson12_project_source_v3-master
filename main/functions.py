import json


def load_all_posts():
    """
    Открывает и считывает все данные из файла
    """
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_by_word(word: str) -> list[dict]:
    """
    Осуществляет поиск по слову
    :param word: слово
    :return: пост
    """
    datas = []
    for post in load_all_posts():
        if word.lower() in post['content'].lower():
            datas.append(post)
    return datas
