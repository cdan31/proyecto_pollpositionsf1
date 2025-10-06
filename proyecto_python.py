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

#Lista de pilotos del 1 al 20
pilotos = []
for contador in range(1, 21):
    tiempo1 = float(input(f"Tiempo 1 del piloto {contador}: "))
    tiempo2 = float(input(f"Tiempo 2 del piloto {contador}: "))
    tiempo3 = float(input(f"Tiempo 3 del piloto {contador}: "))
    
    prom = promedio(tiempo1, tiempo2, tiempo3)
    pilotos.append(prom)

# Primer lugar
m1 = pilotos[0]
for i in range(1, 20):
    if pilotos[i] < m1:
        m1 = pilotos[i]

# Segundo lugar
m2 = float(999999)
for i in range(20):
    if pilotos[i] != m1 and pilotos[i] < m2:
        m2 = pilotos[i]

# Tercer lugar
m3 = float(99999)
for i in range(20):
    if pilotos[i] != m1 and pilotos[i] != m2 and pilotos[i] < m3:
        m3 = pilotos[i]

# Output
print("1er lugar (promedio más rápido):", m1)
print("2do lugar:", m2)
print("3er lugar:", m3)
