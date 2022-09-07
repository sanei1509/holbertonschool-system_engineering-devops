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
        for user in user_json:
            lista_tareas = []
            for task in todos_json:
                if task["userId"] == user["id"]:
                    sub_dic = {}
                    sub_dic['username'] = user['username']
                    sub_dic['task'] = task['title']
                    sub_dic['completed'] = task["completed"]
                    lista_tareas.append(sub_dic)
            todos[user["id"]] = lista_tareas
    # luego de formatear todo como necesitabamos guardamos en el json file
    json.dump(todos, outfile)

except Exception as err:
    print(err)