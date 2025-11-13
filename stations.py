# Módulo que contiene las funciones  relacionadas con la generación de estadísticas para una estación específica
from collections import Counter # < sirve para contar elementos repetidos en una lista, cadena u otro iterable. (Libreria nativa de Python)

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


# Estadísticas por estación 

def numberTripsStation(station_id, station_activity) -> int:  # número de viajes realizados en una estación 

    ''' Funcion que calcula el numero de viajes realizados en una estación '''

    trips = len(station_activity[station_id])
    return trips


def peakHoursEntryStation(station_id, station_activity) -> None:  # horas pico de ingreso a una estación
    
    ''' Funcion que calcula las horas pico de ingreso a una estación '''

    if station_id not in station_activity:
        print(f" \nNo hay registros para la estación {station_id}")
        return

    # Filtrar por station_id el diccionario station_activity y traer los eventos de ingreso
    entries = []
    for user_id, event_type, event_time in station_activity[station_id]: # Recorremos la lista de eventos de la estación
        if event_type == 'IN':
            entries.append(event_time) ## Agregamos a Entries el event_type == 'IN" el cual contiene la hora de ingreso.

    # print(entries) Imprimimos la lista de horas de ingreso.

    if not entries:
        print(f" \nNo hay registros de ingreso para la estación {station_id}")
        return

    hours = [] # Almacenamos las horas de ingreso
    for entry in entries:
        hours.append(entry[:2]) # Agregamos a la lista hours la hora de ingreso extrayendo por slicing
    # print(hours)

    # Usaremos una funcion nativa de Python para contar la frecuencia de cada hora
    hourCounts = Counter(hours) # Es un diccionario con la hora de ingreso como clave y la frecuencia como valor
    maxCount = max(hourCounts.values())

    #Ahora buscamos las horas con el maximo conteo
    peakHours = []
    for hour, count in hourCounts.items(): # Recorremos los items del diccionario hourCounts
        if count == maxCount:
            peakHours.append(hour)

    print(f'\nHoras picos de ingreso a la Estacion {station_id}: ')
    for hour in peakHours:
        print(f'{hour}h:00 - Usuarios: {hourCounts[hour]}')




def peakHoursExitStation(station_id, station_activity) -> None:  # horas pico de salida de una estación

    ''' Funcion que calcula las horas pico de salida de una estación '''

    if station_id not in station_activity:
        print(f" \nNo hay registros para la estación {station_id}")
        return

    # Filtrar por station_id el diccionario station_activity y traer los eventos de ingreso
    exits = []
    for user_id, event_type, event_time in station_activity[station_id]: # Recorremos la lista de eventos de la estación
        if event_type == 'OUT':
            exits.append(event_time) ## Agregamos a Entries el event_type == 'OUT" el cual contiene la hora de salida.

    # print(exits) Imprimimos la lista de horas de salida.

    if not exits:  
        print(f" \n No hay registros de salida para la estación {station_id}")
        return

    hours = [] # Almacenamos las horas de salida
    for exit in exits:
        hours.append(exit[:2]) # Agregamos a la lista hours la hora de salida extrayendo por slicing
    # print(hours)

    # Usaremos una funcion nativa de Python para contar la frecuencia de cada hora
    hourCounts = Counter(hours) 
    maxCount = max(hourCounts.values())

    #Ahora buscamos las horas con el maximo conteo
    peakHours = []
    for hour, count in hourCounts.items():
        if count == maxCount:
            peakHours.append(hour)

    print(f'\n Horas picos de salida de la Estacion {station_id}: ')
    for hour in peakHours:
        print(f'{hour}h:00 - Usuarios: {hourCounts[hour]}')


def mostFrequentOriginStation(station_id, user_activity) -> None:  # estación de origen más frecuente hacia esta estación

    ''' Funcion que calcula la estación de origen más frecuente hacia una estación específica '''

    origin_counts = {}  # station_id_origen -> cantidad de viajes que llegan a station_id

    for user_id, events in user_activity.items():
        open_origin_station_id = None  # None si no hay viaje abierto

        for event in events:
            event_type = event[0]
            event_time = event[1]
            current_station_id = event[2]

            if event_type == 'IN' and open_origin_station_id is None:
                open_origin_station_id = current_station_id

            elif event_type == 'OUT' and open_origin_station_id is not None:
                origin_station_id = open_origin_station_id
                destination_station_id = current_station_id

                if destination_station_id == station_id:
                    if origin_station_id not in origin_counts:
                        origin_counts[origin_station_id] = 0
                    origin_counts[origin_station_id] += 1

                # cerrar viaje
                open_origin_station_id = None

    if not origin_counts:
        print(f"No se encontraron viajes hacia la estación {station_id}")
        return

    # hallar el máximo
    max_count = 0
    for origin_station_id, trip_count in origin_counts.items():
        if trip_count > max_count:
            max_count = trip_count

    # recolectar empates
    most_frequent_origin_ids = []
    for origin_station_id, trip_count in origin_counts.items():
        if trip_count == max_count:
            most_frequent_origin_ids.append(origin_station_id)

    print(f"Origen(es) más frecuente(s) hacia la estación {station_id}:")
    for origin_station_id in most_frequent_origin_ids:
        print(f"{origin_station_id} - Viajes: {origin_counts[origin_station_id]}")


def mostFrequentDestinationStation(station_id, user_activity) -> None:  # estación de destino más frecuente desde esta estación

    ''' Funcion que calcula la estación de destino más frecuente desde una estación específica '''

    destination_counts = {}  # station_id_destino -> cantidad de viajes que salen desde station_id

    for user_id, events in user_activity.items():
        open_origin_station_id = None

        for event in events:
            event_type = event[0]
            event_time = event[1]
            current_station_id = event[2]

            if event_type == 'IN' and open_origin_station_id is None:
                open_origin_station_id = current_station_id

            elif event_type == 'OUT' and open_origin_station_id is not None:
                origin_station_id = open_origin_station_id
                destination_station_id = current_station_id

                if origin_station_id == station_id:
                    if destination_station_id not in destination_counts:
                        destination_counts[destination_station_id] = 0
                    destination_counts[destination_station_id] += 1

                # cerrar viaje
                open_origin_station_id = None

    if not destination_counts:
        print(f"No se encontraron viajes que salgan de la estación {station_id}")
        return

    # hallar el máximo
    max_count = 0
    for destination_station_id, trip_count in destination_counts.items():
        if trip_count > max_count:
            max_count = trip_count

    # recolectar empates
    most_frequent_destination_ids = []
    for destination_station_id, trip_count in destination_counts.items():
        if trip_count == max_count:
            most_frequent_destination_ids.append(destination_station_id)

    print(f"Destino(s) más frecuente(s) desde la estación {station_id}:")
    for destination_station_id in most_frequent_destination_ids:
        print(f"{destination_station_id} - Viajes: {destination_counts[destination_station_id]}")


