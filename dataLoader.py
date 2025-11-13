

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