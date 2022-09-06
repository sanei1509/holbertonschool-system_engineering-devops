#!/usr/bin/python3
""" Export to JSON """
if __name__ == "__main__":
    import requests
    import sys
    import json


try:
    id_user = sys.argv[1]
    # DATA fake en la web
    url_user = "https://jsonplaceholder.typicode.com/users/{}"\
               .format(id_user)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(id_user)
    # get de la DATA
    user_data = requests.get(url_user)
    todos_data = requests.get(url_todos)

    # DATA en json
    user_json = user_data.json()
    todos_json = todos_data.json()

    for dic in json:
        content = "{ "{}": [{"task": "dic["title"]", "completed": TASK_COMPLETED_STATUS, "username": "dic["username"]"}]".format(dic["id"])
        print(content)
    # Itero sobre mis tareas 
    # Luego de que tengo los datos voy a trabajar la exportación
    # abrir el archivo con los permisos necesarios
