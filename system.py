# Módulo que contiene las funciones relacionadas con la generación de estadísticas generales del sistema metro

from math import *
from dataLoader import getInfoFromFile
from collections import Counter


stations = {}
user_activity = {}
station_activity = {}


# Esta funcion calcula la distancia entre dos estaciones consecutivas del metro de acuerdo a sus coordenadas geográficas. Ya esta implementada.
def geodistance(P1, P2):
    """
    Calcula la distancia entre dos estaciones consecutivas del metro
    de acuerdo a sus coordenadas geográficas

    Args:
        P1 (list): Coordenadas (latitud, longitud) del primer punto en grados.
        P2 (list): Coordenadas (latitud, longitud) del segundo punto en grados
        Retorna:
                D (float): Distancia en metros entre los dos puntos.

    Ejemplo:
                P1 = [6.2442, -75.5812]
                P2 = [6.2518, -75.5636]
                distancia = geodistance(P1, P2)
    """
    h = 1600  # Altura sobre el nivel del mar en metros (aproximada)
    pi = 3.141592
    R = 6371009  # Radio medio de la Tierra en metros
    theta1 = pi / 2 - (P1[0] * pi / 180)
    phi1 = P1[1] * pi / 180
    rho1 = R + h
    # Conversion de coordenadas esféricas a cartesianas
    theta2 = pi / 2 - (P2[0] * pi / 180)
    phi2 = P2[1] * pi / 180
    rho2 = R + h
    # Conversion de coordenadas esféricas a cartesianas
    x1 = rho1 * sin(theta1) * cos(phi1)
    x2 = rho2 * sin(theta2) * cos(phi2)
    y1 = rho1 * sin(theta1) * sin(phi1)
    y2 = rho2 * sin(theta2) * sin(phi2)
    z1 = rho1 * cos(theta1)
    z2 = rho2 * cos(theta2)
    # Cálculo de la distancia euclidiana entre los dos puntos
    D = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** (1 / 2)
    return D


# Estadísticas generales del sistema
def totalUsersMetro(user_activity) -> int:  # número total de usuarios en sistema metro
    """Función que calcula el número total de usuarios en el sistema metro."""

    totalUsers = len(user_activity)

    print(f"\nEl numero total de usuarios en el sistema metro es: {totalUsers}")


# ----------------------------------------------------------------------------------


def numberTripsMetro(user_activity) -> int:  # número total de viajes realizados
    """Funcion que calcula el numero total de viajes realizados"""

    trips = 0

    # El user es la llave y entries es la lista de tuplas
    for user, entries in user_activity.items():
        for entry in entries:
            if entry[0] == "IN":
                trips = trips + 1

    print(f" El numero total de viajes realizados son: {trips}")

    return trips


# ----------------------------------------------------------------------------------
## hora pico del sistema metro
def rushHourMetro(user_activity) -> None:
    """Función que calcula la hora pico más recurrente en el sistema metro."""

    hours = []
    for user, logs in user_activity.items():
        for log in logs:
            # verificamos si el evento es 'IN'
            if log[0] == "IN":
                # Extraemos la hora
                hour = log[1][
                    :2
                ]  # Entramos a la 1era posicion de la tupla y luego tomamos los primeros 2 valores
                hours.append(hour)

    if not hours:
        print("\nNo hay eventos de ingreso en el sistema.")

    # Contamos cuantas veces se repite cada hora
    counts = Counter(hours)  # {'06': 5, '07': 3, '09': 1, '08': 1}

    # Algotimo para hallar el maximo de entradas
    max_count = 0

    for hour, count in counts.items():
        if count > max_count:
            max_count = count
            max_hour = hour

    # Hallamos si hay empates y los almacenamos en una lista para mostrarlos
    peakHours = []
    peakHoursFormated = 0
    for hour, count in counts.items():
        if count == max_count:
            peakHours.append(hour)

    print(f"Horas pico {peakHours}, con {max_count} Usuarios")


# ----------------------------------------------------------------------------------


def totalRevenueMetro(user_activity, cost_per_trip=3500) -> int:
    """Función que calcula los ingresos totales del sistema metro."""

    total_revenue = numberTripsMetro(user_activity) * cost_per_trip

    print(f"\nEl ingreso total del sistema metro es: ${total_revenue}")

    return total_revenue


# ----------------------------------------------------------------------------------


def mostPopularRoutesMetro(station_activity) -> None:
    """Función que identifica las rutas más populares en el sistema metro."""

    stations = {}

    # Contamos los eventos por estación
    for station, logs in station_activity.items():
        count = len(logs)
        stations[station] = count  # Guardamos el total de logs por estación

    if not stations:
        print("\nNo hay actividad registrada en las estaciones.")
        return

    max_count = max(
        stations.values()
    )  # Guardamos el valor máximo de entradas (El numero que mas se repite)
    print("\n Rutas más populares en el sistema metro: \n")

    for station, count in stations.items():
        if count == max_count:
            print(f"{station} con {max_count} Usuarios.")


def averageDistanceMetro(
    user_activity, stations
) -> float:  # distancia promedio de viaje en el sistema metro
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

            if event_type == "IN" and origin_station_id is None:
                origin_station_id = station_id
            elif event_type == "OUT" and origin_station_id is not None:
                destination_station_id = station_id

                # Verificamos que existan ambas estaciones en el diccionario 'stations'
                if origin_station_id in stations and destination_station_id in stations:
                    origin_coords = stations[origin_station_id]["coordinates"]
                    dest_coords = stations[destination_station_id]["coordinates"]
                    distance_m = geodistance(origin_coords, dest_coords)
                    total_distance_m += distance_m
                    total_trips += 1

                # Cerramos el viaje actual
                origin_station_id = None

    if total_trips == 0:
        print(
            "\nNo se encontraron viajes completos para calcular la distancia promedio."
        )
        return 0.0

    average_m = total_distance_m / total_trips
    average_km = average_m / 1000.0
    print(
        f"\nDistancia promedio por viaje: {average_m:.2f} m ({average_km:.2f} km) en {total_trips} viajes"
    )
    return average_m


def averageTripsMetro(user_activity) -> int:
    """Función que calcula el número promedio de viajes por usuario en el sistema metro."""

    # Contamos los eventos de ingreso 'IN' para obtener el total de viajes y el numero de usuarios.
    total_trips = 0
    for user_id, events in user_activity.items():
        for event in events:
            if event[0] == "IN":
                total_trips += 1

    # contamos el numero de usuarios en el sistema
    num_users = len(user_activity)

    if num_users == 0:
        print("\n No hay usuarios en el sistema.")
        return 0

    avg = int(total_trips / num_users)  # Calculamos el promedio de viajes por usuario
    print("\nNúmero promedio de viajes por usuario:", avg)

    return avg
