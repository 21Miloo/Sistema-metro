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
            numberTripsStation()
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

# Funcion que retorna el archivo metro.log

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



 #? Funciones para almacenar la informacion en estructuras de datos

def proccessStationsInfo(lines):
    return lines 

def proccessMetroLog(lines):
    return lines

data = getInfoFromFile('stations.info')
print(data)






#! Estructura de datos para informacion del Sistema Metro

# Stations = {
#     Station_Id: {
#         StationName: name,
#         Coordinates: [Latitude, Longitude]
#     }
# }

#! Estructura de datos para Informacion de estaciones

# user_activity = {
#     '69253198': [
#         ('IN', '04:03', '010'),
#         ('OUT', '04:25', '018'),
#     ]
# }
