# Determina la posicion inicial de 20 pilotos de la formula 1 dado sus tiempos de lap. 
# Yo creo que esto es interesante porque las posiciones iniciales de la formula 1 pueden determinar 
# los ganadores de las carreras. 

# Entradas: 
# n=numdecimal 
# nombre de pilotos

# Algoritmo:
# 1.- Establecer lista de posiciones del 1-20 
# 2.- Solicitar nombre del piloto y tiempo de lap: numdecimal
    #2.1- Almacenar nombre del piloto junto con tiempo de lap
# 3.- Solicitar nuevamente nombre del piloto y tiempo de lap:
    #3.1- Almacenar nombre del piloto junto con tiempo de lap
# 4.- Repetir hasta llenar lista de pilotos
# 5.- Si tiempo de lap del piloto > tiempo de lap del piloto que sigue entonces dar poll position 1
    # 5.1 Si No: ponerlo una posicion por debajo del piloto que sigue
       # 5.1.1 Volver a comparar tiempo de lap del piloto con el piloto que sigue
        # 5.1.2 Repetir hasta que tiempo de lap del piloto sea mayor al piloto que sigue o se acabe la lista
# 6.- Mostrar tabla de posiciones del 1-20 pilotos y sus tiempos de lap

# Salidas: 
#n=numdecimal 
#nombre de pilotos
#lista 1-20








#----------------------------------------------------------------------------------------------------------------

# Algoritmo para encontrar el podium (primeros 3 lugares) dado 3 tiempos de lap de 20 pilotos de la formula 1

# Función para calcular el promedio de 3 tiempos
def promedio(tiempo1, tiempo2, tiempo3):
    return (tiempo1 + tiempo2 + tiempo3) / 3

# Función que retorna el promedio (para ordenar)
def obtener_promedio(datos_piloto):
    return datos_piloto[1]

# Lista para guardar los tiempos y promedios de todos los pilotos
pilotos = []

# Recolectar los tiempos y calcular promedios
for numero_piloto in range(1, 21):
    tiempos = []
    for vuelta in range(1, 4):
        tiempo = float(input(f"Piloto {numero_piloto} - Tiempo de la vuelta {vuelta}: "))
        tiempos.append(tiempo)

    prom = promedio(tiempos[0], tiempos[1], tiempos[2])
    pilotos.append([numero_piloto, prom])

# Ordenar a los pilotos por tiempo promedio (el menor = más rápido)
pilotos.sort(key=obtener_promedio)

# Mostrar el podio (top 3)
print("1er lugar: Piloto", pilotos[0][0], "con un tiempo promedio de", pilotos[0][1])
print("2do lugar: Piloto", pilotos[1][0], "con un tiempo promedio de", pilotos[1][1])
print("3er lugar: Piloto", pilotos[2][0], "con un tiempo promedio de", pilotos[2][1])
