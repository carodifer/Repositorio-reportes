from datos import cargar_datos, guardar_datos
import mascotas
import dueños
import citas


def main():
    datos = cargar_datos()

    while True:
        print("\n===== REGISTRO DE VETERINARIA =====")
        print("1. Registrar Mascota")
        print("2. Registrar Dueño")
        print("3. Agendar Cita")
        print("4. Consultas")
        print("5. Eliminar Datos")
        print("6. Guardar y Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mascotas.registrar_mascota(datos)
        elif opcion == "2":
            dueños.registrar_dueño(datos)
        elif opcion == "3":
            citas.agendar_cita(datos)
        elif opcion == "4":
            submenu_consultas(datos)
        elif opcion == "5":
            submenu_eliminar(datos)
        elif opcion == "6":
            guardar_datos(datos)
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción inválida.")


def submenu_consultas(datos):
    print("\n--- Consultas ---")
    print("1. Listar Mascotas")
    print("2. Listar Dueños")
    print("3. Listar Citas")
    print("4. Volver")

    op = input("Seleccione: ")

    if op == "1":
        mascotas.listar_mascotas(datos)
    elif op == "2":
        dueños.listar_dueños(datos)
    elif op == "3":
        citas.listar_citas(datos)


def submenu_eliminar(datos):
    print("\n--- Eliminar ---")
    print("1. Eliminar Mascota")
    print("2. Eliminar Dueño")
    print("3. Eliminar Cita")
    print("4. Volver")

    op = input("Seleccione: ")

    if op == "1":
        mascotas.eliminar_mascota(datos)
    elif op == "2":
        dueños.eliminar_dueño(datos)
    elif op == "3":
        citas.eliminar_cita(datos)


if __name__ == "__main__":
    main()
