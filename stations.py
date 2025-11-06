# Módulo que contiene las funciones relacionadas con la generación de estadísticas para una estación específica


# print('\n Seleccione una Opcion: \n \n', '1. Usuarios totales S.M \n', '2. Trayectos mas populares \n', '3. Cantidad de Viajes \n', '4. Horas pico mas recurrentes \n', '5. Ingresos totales \n', '6. Volver al menu anterior \n')


def systemMetroStats():

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

    option = input("Opcion: ")

    flag = True

    while flag:

        if option == "1":
            totalUsersMetro()
            flag = False
        elif option == "2":
            rushHourMetro()
            flag = False

        elif option == "3":
            averageDistanceMetro()
            flag = False

        elif option == "4":
            totalRevenueMetro()
            flag = False

        elif option == "5":
            averageTripsMetro()
            flag = False

        elif option == "6":
            mostPopularRoutesMetro()
            flag = False

        elif option == "7":
            flag = False


systemMetroStats()



# Estadísticas por estación
def numberTripsStation(station_id):  # número de viajes realizados en una estación
    pass


def peakHoursEntryStation(station_id):  # horas pico de ingreso a una estación
    pass


def peakHoursExitStation(station_id):  # horas pico de salida de una estación
    pass


def mostFrequentOriginStation(station_id):  # estación de origen más frecuente
    pass


def mostFrequentDestinationStation(station_id):  # estación de destino más frecuente
    pass