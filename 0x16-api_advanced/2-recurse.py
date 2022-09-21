#!/usr/bin/python3
"""
Crear una función recursiva para extraer una lista que contenga los titulos de
todos los hot articles del subreddit pasado,
Return None sino se encuentran los mismos
"""
import requests


def recurse(subreddit, hot_list=[]):
	