import csv
from clients import Client


def get_data_from_csv(file):
    """
    Funcion para obtener la informacion del csv.
    Recibe como parametro una direccion de archivo.
    Devuelve un diccionario.
    """
    # Abrimos el CSV.
    csv_data = {}
    with open(file) as csv_file:
        # Obtenemos todos los usuarios
        rows = csv.reader(csv_file, delimiter=',')
        # Get first line of clients (headers)
        all_rows = list(rows)
        headers = all_rows.pop(0)
        csv_data = {
            'headers': headers,
            'data': all_rows
        }
    return csv_data


def get_column_position(headers, column):
    """
    Funcion para obtener la posicion de una columna.
    Recibe las columnas y la columna que quiere saber la posicion.
    Devuelve la posicion o None.
    """
    for i, header in enumerate(headers):
        if header == column:
            return i


def search_in_csv(data, column_to_search, data_to_search):
    """
    Funcion para buscar dentro de un csv.
    Recibe como parametro un diccionario con informacion,
    la columna y el dato a buscar
    """
    column = get_column_position(data['headers'], column_to_search)
    for row in data['data']:
        if row[column] == str(data_to_search):
            return row
    return []


def last_row(data):
    """
    Funcion que devuelve la ultima linea de una lista.
    """
    return data['data'][-1]


def get_clients():
    """
    Funcion para obtener los clientes de un csv.
    Lo retorna en una lista.
    """
    clients = []
    csv_data = get_data_from_csv('files/clientes.csv')
    clients_data = csv_data['data']
    for client in clients_data:
        clients.append(Client(*client))
    return clients

def create_user_in_csv(user, file):
    """
    Funcion para crear un usuario en un csv.
    """
    # Obtener el ultimo
    with open(file, mode='a') as csv_file:
        user_writer = csv.writer(csv_file, delimiter='\n', quoting=csv.QUOTE_NONE, escapechar='\n')

        user_writer.writerow([user])
        return True
