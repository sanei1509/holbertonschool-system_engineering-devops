#!/usr/bin/python3
"""
Crear una función recursiva para extraer una lista que contenga los titulos de
todos los hot articles del subreddit pasado,
Return None sino se encuentran los mismos
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    task 5 -> recursive looking for
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

        headers = requests.utils.default_headers()
        headers.update({"User-Agent": "Mozila/5.0"})

        res = requests.get(url, headers=headers, params={'after': after},
                           allow_redirects=False)

        content_json = res.json()
        articles = content_json["data"]["children"]

        for titulo in articles:
            hot_list.append(titulo["data"]["title"])

        after = content_json["data"]["after"]

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return None
