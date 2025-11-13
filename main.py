# Juan Camilo Lopez
# Grupo 8

# Facultad de Ingenieria
# Universidad de Antioquia

# Implemente aquí los menús y el programa principal que invoca las funciones de los otros módulos


# import test as ts
from dataLoader import getInfoFromFile
from system import *  ## Cargamos todas las funciones del modulo system.py
from stations import *  ## Cargamos todas las funciones del modulo stations.py


# Cargamos los datos
stations = getInfoFromFile("data/stations.info")
user_activity, station_activity = getInfoFromFile("data/metro_100k.log")


# ---------------------Funciones a Invocar------------------------------


def systemMetroStats():

    while True:

        print("\n--- ESTADÍSTICAS DEL SISTEMA METRO ---")

        print(
            "\n Seleccione una Opcion: \n \n",
            "1. Número total de usuarios y viajes S.M  \n",
            "2. Hora pico mas recurrentes \n",
            "3. Distancia promedio de viaje \n",
            "4. Ingresos totales \n",
            "5. Numero promedio de viajes \n",
            "6. Trayectos mas populares \n",
            "7. Volver al Menu anterior \n",
        )

        option = input(
            "Opcion: "
        ).strip()  # Strip elimina espacios en blanco al inicio y al final

        if option == "1":
            totalUsersMetro(user_activity)
            numberTripsMetro(user_activity)
        elif option == "2":
            rushHourMetro(user_activity)
        elif option == "3":
            averageDistanceMetro(user_activity, stations)

        elif option == "4":
            totalRevenueMetro(user_activity)

        elif option == "5":
            averageTripsMetro(user_activity)

        elif option == "6":
            mostPopularRoutesMetro(user_activity)

        elif option == "7":
            break
        else:
            print("\n Opción inválida. Intente de nuevo.")


# --------------------------------------------------------------------------------------------


def menuStationStats():

    while flag:

        print("\n--- ESTADÍSTICAS POR ESTACIÓN ---")

        print(
            "\n Seleccione una Opcion: \n \n",
            "1. Número de viajes realizados en una estación \n",
            "2. Horas pico de ingreso a una estación \n",
            "3. Horas pico de salida de una estación \n",
            "4. Estación de origen más frecuente \n",
            "5. Estación de destino más frecuente \n",
            "6. Volver al Menu anterior \n",
        )

        option = input("\nOpción: ").strip()

        if option == "1":
            station_id = input("Ingrese el ID de la estación: ")
            numberTripsStation(station_id, station_activity)
        elif option == "2":
            station_id = input("Ingrese el ID de la estación: ")
            peakHoursEntryStation(station_id, station_activity)
        elif option == "3":
            station_id = input("Ingrese el ID de la estación: ")
            peakHoursExitStation(station_id, station_activity)
        elif option == "4":
            station_id = input("Ingrese el ID de la estación: ")
            mostFrequentOriginStation(station_id, user_activity)
        elif option == "5":
            station_id = input("Ingrese el ID de la estación: ")
            mostFrequentDestinationStation(station_id, user_activity)
        elif option == "6":
            break
        else:
            print("\n Opción inválida. Intente de nuevo.")


# ---------------------Menu Principal------------------------------
# Punto de entrada del programa

while True:
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
        systemMetroStats()
    elif option == "2":
        menuStationStats()
    elif option == "3":
        print("Gracias por usar el sistema de estadísticas del metro. ¡Hasta luego!")
        break
    else:
        print("\n Opción inválida. Intente de nuevo.")
