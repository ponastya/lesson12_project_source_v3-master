import json
def add_post():
    with open('posts.json', 'b', encoding='utf-8') as f:
        return json.load()