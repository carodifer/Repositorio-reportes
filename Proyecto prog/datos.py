import json

RUTA_ARCHIVO = "datos.json"


def cargar_datos():
    try:
        with open(RUTA_ARCHIVO, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        datos = {"mascotas": [], "duenos": [], "citas": []}
        guardar_datos(datos)
        return datos


def guardar_datos(datos):
    with open(RUTA_ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)
