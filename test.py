"""from requests import get, post, delete

cookies = dict(session='session cookies here')
print(post('http://localhost:8000/api/v1/news',
           json={'title': 'Заголовок', 'content': 'Текст новости', 'user_id': 1}, cookies=cookies).json())
print(get('http://localhost:8000/api/v1/news').json())
print(delete('http://localhost:8000/api/v1/news/5', cookies=cookies).json())
print(get('http://localhost:8000/api/v1/news').json())"""