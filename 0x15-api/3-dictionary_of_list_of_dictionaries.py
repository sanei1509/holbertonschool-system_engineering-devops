#!/usr/bin/python3
""" Dictionary of list of dictionaries """
if __name__ == "__main__":
    import requests
    import json


try:
    # DATA fake en la web
    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    # get de la DATA
    user_data = requests.get(url_user)
    todos_data = requests.get(url_todos)

    user_json = user_data.json()
    todos_json = todos_data.json()

    with open("todo_all_employees.json", "w", newline='') as outfile:
        todos = {}
        # itero sobre los usuarios
        for user in user_json:
            lista_tareas = []
            # itero sobre las tareas
            for task in todos_json:
                # (comparo) necesito ir almacenando usuario y respectivas
                if task["userId"] == user["id"]:
                    sub_dic = {}
                    sub_dic['username'] = user['username']
                    sub_dic['task'] = task['title']
                    sub_dic['completed'] = task["completed"]
                    lista_tareas.append(sub_dic)
            # finalizo de analizar un usuario y almaceno con su lista de tareas
            todos[user["id"]] = lista_tareas
        json.dump(todos, outfile)

except Exception as err:
    print(err)
