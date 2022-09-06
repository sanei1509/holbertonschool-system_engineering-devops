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

    dictionary = {}
    lista_tareas = []
    for task in todos_json:
        sub_dic = {}
        sub_dic['task'] = task['title']
        sub_dic['completed'] = task['completed']
        sub_dic['username'] = user_json["username"]
        # armo mi propio formato de tareas
        lista_tareas.append(sub_dic)
    dictionary[id_user] = lista_tareas

    print(dictionary)

    with open("{}.json".format(id_user), "w") as outfile:
        json.dump(dictionary, outfile)

except Exception as err:
    print(err)
