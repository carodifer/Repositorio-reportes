def registrar_mascota(datos):
    print("\n--- Registrar Mascota ---")
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    dueño = input("Nombre del dueño: ")

    mascota = {
        "nombre": nombre,
        "especie": especie,
        "raza": raza,
        "edad": edad,
        "dueño": dueño
    }

    datos["mascotas"].append(mascota)
    print("Mascota registrada correctamente.")


def listar_mascotas(datos):
    print("\n--- Lista de Mascotas ---")
    if not datos["mascotas"]:
        print("No hay mascotas registradas.")
        return

    for m in datos["mascotas"]:
        print(f"- {m['nombre']} ({m['especie']}), Dueño: {m['dueño']}")


def actualizar_mascota(datos):
    print("\n--- Actualizar Mascota ---")
    nombre = input("Ingrese el nombre de la mascota a actualizar: ")

    for mascota in datos["mascotas"]:
        if mascota["nombre"] == nombre:
            print("Dejar vacío para mantener el valor actual.")
            especie_input = input(f"Especie ({mascota['especie']}): ")
            mascota["especie"] = especie_input or mascota["especie"]
            raza_input = input(f"Raza ({mascota['raza']}): ")
            mascota["raza"] = raza_input or mascota["raza"]
            edad_input = input(f"Edad ({mascota['edad']}): ")
            mascota["edad"] = edad_input or mascota["edad"]
            dueño_input = input(f"Dueño ({mascota['dueño']}): ")
            mascota["dueño"] = dueño_input or mascota["dueño"]

            print("Mascota actualizada.")
            return
          
    print(" No se encontró la mascota.")


def eliminar_mascota(datos):
    print("\n--- Eliminar Mascota ---")
    nombre = input("Ingrese el nombre de la mascota a eliminar: ")

    for mascota in datos["mascotas"]:
        if mascota["nombre"] == nombre:
            datos["mascotas"].remove(mascota)
            print(" Mascota eliminada.")
            return

    print(" No se encontró la mascota.")
