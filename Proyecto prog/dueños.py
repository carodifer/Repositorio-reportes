def registrar_dueño(datos):
    print("\n--- Registrar Dueño ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")

    dueño = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
    }

    datos["dueños"].append(dueño)
    print("Dueño registrado correctamente.")


def listar_dueños(datos):
    print("\n--- Lista de Dueños ---")
    if not datos["dueños"]:
        print("No hay dueños registrados.")
        return

    for d in datos["dueños"]:
        print(f"- {d['nombre']} | Tel: {d['telefono']} | "
              f"Dir: {d['direccion']}")


def eliminar_dueño(datos):
    print("\n--- Eliminar Dueño ---")
    nombre = input("Nombre del dueño: ")

    existe = False
    for d in datos["dueños"]:
        if d["nombre"] == nombre:
            existe = True
            break
    if not existe:
        print("No se encontró el dueño.")
        return

    datos["dueños"] = [d for d in datos["dueños"] if d["nombre"] != nombre]
    datos["dueños"] = [d for d in datos["dueños"] if d["nombre"] != nombre]

    print("Dueño eliminado.")
