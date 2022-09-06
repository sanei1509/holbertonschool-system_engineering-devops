#!/usr/bin/python3
""" Export to CSV """
if __name__ == "__main__":
    import csv
    import requests
    import sys


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

    # Itero sobre mis tareas
    # Luego de que tengo los datos voy a trabajar la exportación
    # abrir el archivo con los permisos necesarios


    # Formato a imprimir en el csv
    contenido = []
    for dic in todos_json:
        contenido.append(dic["userId"])
        contenido.append(user_json["name"])
        contenido.append(dic["completed"])
        contenido.append(dic["title"])

    with open("{}.csv".format(user_json["id"]), 'w') as file:
        # escribo en formato csv dentro del archivo
        write = csv.writer(file) 

        # creo una fila en el archivo CSV
        write.writerow(contenido)

except Exception as err:
    print("error en la recolección de datos {}".format(err))
