# Implemente aquí los menús y el programa principal que invoca las funciones de los otros módulos

import test as ts

flag = True

while flag:
    print(" \n Bienvenido al Sistema de Estadísticas del Metro")
    print("=" * 50)
    print("\nEscoja una opción:")
    print("1. Estadísticas del Sistema Metro")
    print("2. Estadísticas por Estación")
    print("3. Salir")

    option = input(
        "\nOpción: "
    ).strip()  # Strip elimina espacios en blanco al inicio y al final

    if option == "1":
        ts.systemMetroStats()

    elif option == "2":
        ts.menuStationStats()

    elif option == "3":
        print("Gracias por usar el sistema de estadísticas del metro. ¡Hasta luego!")
        flag = False

    else:
        print("\n❌ Opción inválida. Intente de nuevo.")
