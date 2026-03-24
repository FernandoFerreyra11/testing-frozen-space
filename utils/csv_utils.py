import csv
import os


def read_users_csv(file_path):
    """Lee credenciales de un CSV y devuelve una lista de dicts"""
    users = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No se encontro el archivo CSV: {file_path}")

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        # Detectar delimitador (; o ,)
        sample = csvfile.read(1024)
        csvfile.seek(0)
        delimiter = ';' if ';' in sample else ','
        reader = csv.DictReader(csvfile, delimiter=delimiter)

        for row in reader:
            users.append({k.strip(): v.strip() for k, v in row.items()})

    return users


def get_user_by_index(users, index):
    """Devuelve credencial en el indice indicado y lanza IndexError si no existe"""
    if index < 0 or index >= len(users):
        raise IndexError(f"Indice de usuario fuera de rango: {index}")
    return users[index]
