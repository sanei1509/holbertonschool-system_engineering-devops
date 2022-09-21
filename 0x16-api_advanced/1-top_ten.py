#!/usr/bin/python3
"""
Extraer de la api de reddit [ first 10 hot posts ]
api de reddit => "https://www.reddit.com/dev/api/#GET_hot"
"""
import requests


def top_ten(subreddit):
    """función para listar los 10 post más populares"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    res = requests.get(url, headers={"User-Agent": "Mozila/5.0"})

    # necesitamos la data en formato json para poder buscar lo solicitado
    content_json = res.json()
    if (res.status_code == 200):
        # buscamos los hot posts
        populares = content_json["data"]["children"]
        for post in populares:
            print(post["data"]["title"])
    else:
        print(None)
