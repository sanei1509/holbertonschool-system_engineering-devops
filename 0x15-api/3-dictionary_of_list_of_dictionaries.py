#!/usr/bin/python3
""" Dictionary of list of dictionaries """
if __name__ == "__main__":
    import requests
    import sys
    import json


try:
    id_user = sys.argv[1]
    # DATA fake en la web
    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    # get de la DATA
    user_data = requests.get(url_user)
    todos_data = requests.get(url_todos)

    DATA en json
    user_json = user_data.json()
    todos_json = todos_data.json()

    dictionary = {}
    lista_tareas = []
    for task in todos_json:
        sub_dic = {}
        sub_dic['task'] = task['title']
        sub_dic['completed'] = task['completed']
        sub_dic['username'] = user_json["username"]
        lista_tareas.append(sub_dic)
    dictionary["{}".format(user_json)] = lista_tareas

    print(dictionary)

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(dictionary, outfile)

except Exception as err:
    print(err)