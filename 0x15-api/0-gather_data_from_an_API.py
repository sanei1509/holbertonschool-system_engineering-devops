#!/usr/bin/python3
""" recolectar data de una api """
"""
using https://jsonplaceholder.typicode.com/:
    - devolver la información sobre su progreso en todolist
    - recibir como parametro ID del usuario
"""
if __name__ == "__main__":
    import requests
    import sys

    # al ser un proceso asíncrono
    try:
        id_user = sys.argv[1]
        # url -> json con data sobre usuarios en un todolist
        url_user = "https://jsonplaceholder.typicode.com/users/{}".format(id_user)
        url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id_user)
        #DATA
        user_data = requests.get(url_user)
        todos_data = requests.get(url_todos)
        # DATA JSON para poder trabajar sobre los datos
        user_json = user_data.json()
        todos_json = todos_data.json()
        # formato a mostrar
        task_completed = 0
        task_total = 0
        for dic in todos_json:
            if(dic["completed"] == True):
                # print(dic["completed"])
                task_completed += 1
            # print(dic["completed"])
            task_total += 1
        print("========formato===========")
        print("Employee {} is done with tasks({}/{}):".format(user_json["name"], task_completed, task_total))
    except Exception as err:
        print(f"error en la recolección de datos {err}")