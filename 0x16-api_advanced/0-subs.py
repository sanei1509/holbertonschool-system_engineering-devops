#!/usr/bin/python3
"""
extraer de la api de reddit el numero de subscriptores (total)
- asegurandonos de configurar un agente de usuario personalizado
"""
import requests


def number_of_subscribers(subreddit):
    "función para realizar la solicitud"
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers={"User-Agent": "Mozila/5.0"})
    res_json = res.json()
    if (res.status_code == 200):
        return res_json["data"]["subscribers"]
    else:
        return 0
