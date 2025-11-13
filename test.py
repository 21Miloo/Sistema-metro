from collections import Counter

# Functions to be tested

# general stats


# def menu():  # Depende de la opcion escogida por el usuario, invocamos el menu correspondiente.

#     flag = True

#     while flag:
#         print(" \n Bienvenido al Sistema de Estadísticas del Metro")
#         print("=" * 50)
#         print("\nEscoja una opción:")
#         print("1. Estadísticas del Sistema Metro")
#         print("2. Estadísticas por Estación")
#         print("3. Salir")

#         option = input(
#             "\nOpción: "
#         ).strip()  # Strip elimina espacios en blanco al inicio y al final

#         if option == "1":
#             systemMetroStats()

#         elif option == "2":
#             menuStationStats()

#         elif option == "3":
#             print(
#                 "Gracias por usar el sistema de estadísticas del metro. ¡Hasta luego!"
#             )
#             flag = False

#         else:
#             print("\n❌ Opción inválida. Intente de nuevo.")


# --------------------------------------------------------------------------------------------


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
        ).strip()  ## Se usa el input dentro del while para que se pida la opcion cada vez que se itere el ciclo y no se quede con la misma opcion anterior

        if option == "1":
            totalUsersMetro()
            numberTripsMetro()
        elif option == "2":
            rushHourMetro()
        elif option == "3":
            averageDistanceMetro()

        elif option == "4":
            totalRevenueMetro()

        elif option == "5":
            averageTripsMetro()

        elif option == "6":
            mostPopularRoutesMetro()

        elif option == "7":
            break
        else:
            print("\n❌ Opción inválida. Intente de nuevo.")


# --------------------------------------------------------------------------------------------


def menuStationStats():

    flag = True

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

        option = input()

        if option == "1":
            station_id = input("Ingrese el ID de la estación: ")
            numberTripsStation(station_id)
        elif option == "2":
            peakHoursEntryStation()
        elif option == "3":
            peakHoursExitStation()
        elif option == "4":
            mostFrequentOriginStation()
        elif option == "5":
            mostFrequentDestinationStation()
        elif option == "6":
            flag = False
        else:
            print("\n❌ Opción inválida. Intente de nuevo.")



### -------------------------------------------------------------------------------------------------------------------------------------------

def getInfoFromFile(file):

  f = open(file)
  lines = f.readlines() # <-- Leemos todas las lineas del archivo y las guardames en un lista.
  f.close() # Cerramos el archivo}

# depende de la terminacion del archivo, llamaremos una funcion, la cual contiene el algoritmo para extraer la informacion del archivo en una estructura de datos.
  if file.endswith('.info'):
    return proccessStationsInfo(lines)
  
  elif file.endswith('.log'):
    return proccessMetroLog(lines) 
  
  else: 
    return None


 #? Funciones para almacenar la informacion en estructuras de datos -----------------------------------------------------------------------------------------------------------


def proccessStationsInfo(lines):
  
  stations = {}
  
# Recorremos cada linea del archivo a partir de la primera linea
# En cada Linea se van a crear un array con las data dividida
# Asignamos a el objeto cada posicion del array a su respectiva llave en el diccionario
  for line in lines[1:]:
      
      data = line.split(',')
      data[3] = data[3].strip() # Eliminamos el salto de linea del final de la linea

      stations[data[1]] = { 'name': data[0], 'coordinates': [float(data[2]), float(data[3])] }

  return stations

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def proccessMetroLog(lines):

    user_activity = {}
    station_activity = {}

    # Recorremos las líneas (omitimos el encabezado)
    for line in lines[1:]:
        data = line.split() # Split elimina los espacios en blanco y saltos de linea y crea un array con la data dividida

        user_id = data[1]
        event_type = data[3]
        event_time = data[2]
        station_id = data[0]

        #***** Diccionario user_activity *****
        # Si el usuario no existe en el diccionario, lo creamos con una lista vacía
        if user_id not in user_activity:
            user_activity[user_id] = []

        # Agregamos el nuevo evento a su lista
        user_activity[user_id].append((event_type, event_time, station_id))

        #***** Diccionario station_activity *****

        if station_id not in station_activity:
            station_activity[station_id] = []

        # Agregamos el nuevo evento a su lista
        station_activity[station_id].append((user_id, event_type, event_time))


    return user_activity, station_activity  # Retornamos las 2 estructuras de datos la cual tomaremos depende de nuestra conveniencia.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# data = getInfoFromFile('metro.log')
# print(data)


#! Estructura de datos para informacion del Sistema Metro

# Stations = {
#     Station_Id: {
#         StationName: name,
#         Coordinates: [Latitude, Longitude]
#     }
# }

#! Estructura de datos para Informacion de Usuarios 

# user_activity = {
#     '69253198': [
#         ('IN', '04:03', '010'),
#         ('OUT', '04:25', '018'),
#     ]
# }

#! Estrcutura de datos para Informacion de Estaciones

# station_activity = {
#     '010': [
#         ('69253198', 'IN', '04:03'),
#         ('08707722', 'IN', '04:04')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funciones Pruebas

station_activity = {
    '010': [
        ('69253198', 'IN', '04:03'),
        ('08707722', 'IN', '04:04')
    ]
}

def peakHoursEntryStation(station_id, station_activity):  # horas pico de ingreso a una estación
    
    # Filtrar por station_id el diccionario station_activity y traer los eventos de ingreso

    entries = []

    # Tema desenpaquetado de tuplas
    for user_id, event_type, event_time in station_activity[station_id]: # Recorremos la lista de eventos de la estación
        if event_type == 'IN': 
            entries.append(event_time)  ## Agregamos a Entries el event_type == 'IN" el cual contiene la hora de ingreso.

    print(entries)

    if not entries:
        print(f" \nNo hay registros de ingreso para la estación {station_id}")
        return

    hours = [] # Almacenamos las horas de ingreso
    for entry in entries:
        hours.append(entry[:2]) # Agregamos a la lista hours la hora de ingreso extrayendo por slicing
    print(hours)

        # Usaremos una funcion nativa de Python para contar la frecuencia de cada hora
    hourCounts = Counter(hours) 
    print(hourCounts)
    maxCount = max(hourCounts.values()) # Devuelve el valor maximo de las horas de ingreso (el que mas se repite)
    print(maxCount)
    # Salida: Counter({'04': 2}) #

    peakHours = []
    for hour, count in hourCounts.items():
        if count == maxCount:
            peakHours.append(hour)

    print(f'\n Horas picos de ingreso a la Estacion {station_id}: ')
    for hour in peakHours:
        print(f'{hour}h')

# peakHoursEntryStation('010', station_activity)



user_activity = {
    '69253198': [
        ('IN', '04:03', '010'),
        ('OUT', '04:25', '018'),
    ]
}

# Funcion Mal planteada ------------------------------------------
# def numberTripsMetro(user_activity):  # número total de viajes realizados
    
#     # Debemos de contar la cantidad de viajes realizados por cada usuario 'IN'
#     trips = 0
#     for user_id, event_type, event_time in user_activity.values(): # Recorremos los valores del diccionario user_activity
#         if event_type == 'IN':
#             trips += 1
#     print(f'\nEl numero total de viajes realizados en el sistema metro es: {trips}')


def numberTripsMetro(user_activity):
    trips = 0
    for events in user_activity.values():                # lista de eventos del usuario
        for event_type, event_time, station_id in events:
            if event_type == 'IN':
                trips += 1
    print(f'\nEl numero total de viajes realizados en el sistema metro es: {trips}')



numberTripsMetro(user_activity)


## ------------- Funcion SystemMetroStats -------------


def averageTripsMetro(user_activity):
    
    # Contamos los eventos de ingreso 'IN' para obtener el total de viajes y el numero de usuarios.
    total_trips = 0
    for user_id, events in user_activity.items():
        for event in events:
            event_type, event_time, station_id = event
            if event_type == 'IN':
                total_trips += 1

    # contamos el numero de usuarios en el sistema
    num_users = len(user_activity)

    if num_users == 0:
        print("\n No hay usuarios en el sistema.")

    avg = total_trips / num_users # Calculamos el promedio de viajes por usuario
    print("\nNúmero promedio de viajes por usuario:", avg)
    

# averageTripsMetro(user_activity)

#! Estructura de datos

# station_activity = {
#     '010': [
#         ('69253198', 'IN', '04:03'),
#         ('08707722', 'IN', '04:04')


def mostPopularRoutesMetro(station_activity) -> None:
    '''Función que identifica las rutas más populares en el sistema metro.'''

    stations = {}  # Debe ser un diccionario, no una lista

    # Contamos los eventos por estación
    for station, logs in station_activity.items():
        count = len(logs)
        stations[station] = count  # Guardamos el total de logs por estación

    if not stations:
        print("\nNo hay actividad registrada en las estaciones.")
        return
    
    # Buscamos el valor máximo
    max_count = max(stations.values())  # Guardamos el valor máximo de entradas (El numero que mas se repite)
    print("\n Rutas más populares en el sistema metro: \n")

    for station, count in stations.items():
        if count == max_count:
            print(f"{station} con {max_count} Usuarios.")

    
# mostPopularRoutesMetro(station_activity)

def averageDistanceMetro(user_activity, stations) -> float:  # distancia promedio de viaje en el sistema metro
    """
    Calcula la distancia promedio por viaje en todo el sistema.
    - Un viaje se considera como un par IN -> OUT del mismo usuario.
    - Usa las coordenadas de 'stations' y la función geodistance para medir.
    """
    total_distance_m = 0.0
    total_trips = 0

    # Recorremos cada usuario y emparejamos IN -> OUT en orden temporal
    for _user, events in user_activity.items():
        # Emparejar en el orden original de los eventos (sin sorted ni lambda)
        origin_station_id = None

        for event in events:
            event_type = event[0]
            station_id = event[2]

            if event_type == 'IN' and origin_station_id is None:
                origin_station_id = station_id
            elif event_type == 'OUT' and origin_station_id is not None:
                destination_station_id = station_id

                # Verificamos que existan ambas estaciones en el diccionario 'stations'
                if origin_station_id in stations and destination_station_id in stations:
                    origin_coords = stations[origin_station_id]['coordinates']
                    dest_coords = stations[destination_station_id]['coordinates']
                    distance_m = geodistance(origin_coords, dest_coords)
                    total_distance_m += distance_m
                    total_trips += 1

                # Cerramos el viaje actual
                origin_station_id = None

    if total_trips == 0:
        print("\nNo se encontraron viajes completos para calcular la distancia promedio.")
        return 0.0

# averageDistanceMetro(user_activity, stations)