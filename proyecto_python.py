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

# Función para calcular el promedio de tres tiempos de lap de los pilotos
def promedio(tiempo1, tiempo2, tiempo3):
    return (tiempo1 + tiempo2 + tiempo3) / 3

# Input: 3 tiempos para cada piloto
p1 = promedio(
    float(input("Tiempo 1 del piloto 1: ")),
    float(input("Tiempo 2 del piloto 1: ")),
    float(input("Tiempo 3 del piloto 1: ")))
p2 = promedio(
    float(input("Tiempo 1 del piloto 2: ")),
    float(input("Tiempo 2 del piloto 2: ")),
    float(input("Tiempo 3 del piloto 2: ")))
p3 = promedio(
    float(input("Tiempo 1 del piloto 3: ")),
    float(input("Tiempo 2 del piloto 3: ")),
    float(input("Tiempo 3 del piloto 3: ")))
p4 = promedio(
    float(input("Tiempo 1 del piloto 4: ")),
    float(input("Tiempo 2 del piloto 4: ")),
    float(input("Tiempo 3 del piloto 4: ")))
p5 = promedio(
    float(input("Tiempo 1 del piloto 5: ")),
    float(input("Tiempo 2 del piloto 5: ")),
    float(input("Tiempo 3 del piloto 5: ")))
p6 = promedio(
    float(input("Tiempo 1 del piloto 6: ")),
    float(input("Tiempo 2 del piloto 6: ")),
    float(input("Tiempo 3 del piloto 6: ")))
p7 = promedio(
    float(input("Tiempo 1 del piloto 7: ")),
    float(input("Tiempo 2 del piloto 7: ")),
    float(input("Tiempo 3 del piloto 7: ")))
p8 = promedio(
    float(input("Tiempo 1 del piloto 8: ")),
    float(input("Tiempo 2 del piloto 8: ")),
    float(input("Tiempo 3 del piloto 8: ")))
p9 = promedio(
    float(input("Tiempo 1 del piloto 9: ")),
    float(input("Tiempo 2 del piloto 9: ")),
    float(input("Tiempo 3 del piloto 9: ")))
p10 = promedio(
    float(input("Tiempo 1 del piloto 10: ")),
    float(input("Tiempo 2 del piloto 10: ")),
    float(input("Tiempo 3 del piloto 10: ")))
p11 = promedio(
    float(input("Tiempo 1 del piloto 11: ")),
    float(input("Tiempo 2 del piloto 11: ")),
    float(input("Tiempo 3 del piloto 11: ")))
p12 = promedio(
    float(input("Tiempo 1 del piloto 12: ")),
    float(input("Tiempo 2 del piloto 12: ")),
    float(input("Tiempo 3 del piloto 12: ")))
p13 = promedio(
    float(input("Tiempo 1 del piloto 13: ")),
    float(input("Tiempo 2 del piloto 13: ")),
    float(input("Tiempo 3 del piloto 13: ")))
p14 = promedio(
    float(input("Tiempo 1 del piloto 14: ")),
    float(input("Tiempo 2 del piloto 14: ")),
    float(input("Tiempo 3 del piloto 14: ")))
p15 = promedio(
    float(input("Tiempo 1 del piloto 15: ")),
    float(input("Tiempo 2 del piloto 15: ")),
    float(input("Tiempo 3 del piloto 15: ")))
p16 = promedio(
    float(input("Tiempo 1 del piloto 16: ")),
    float(input("Tiempo 2 del piloto 16: ")),
    float(input("Tiempo 3 del piloto 16: ")))
p17 = promedio(
    float(input("Tiempo 1 del piloto 17: ")),
    float(input("Tiempo 2 del piloto 17: ")),
    float(input("Tiempo 3 del piloto 17: ")))
p18 = promedio(
    float(input("Tiempo 1 del piloto 18: ")),
    float(input("Tiempo 2 del piloto 18: ")),
    float(input("Tiempo 3 del piloto 18: ")))
p19 = promedio(
    float(input("Tiempo 1 del piloto 19: ")),
    float(input("Tiempo 2 del piloto 19: ")),
    float(input("Tiempo 3 del piloto 19: ")))
p20 = promedio(
    float(input("Tiempo 1 del piloto 20: ")),
    float(input("Tiempo 2 del piloto 20: ")),
    float(input("Tiempo 3 del piloto 20: ")))

# Función para determinar si un tiempo es menor que otro
def menor(tiempo_a, tiempo_b):
    if tiempo_a < tiempo_b:
        return True
    else:
        return False
    
# Encontrar el tiempo menor (el lap más rápido)
m1 = p1
if menor(p2, m1): m1 = p2
if menor(p3, m1): m1 = p3
if menor(p4, m1): m1 = p4
if menor(p5, m1): m1 = p5
if menor(p6, m1): m1 = p6
if menor(p7, m1): m1 = p7
if menor(p8, m1): m1 = p8
if menor(p9, m1): m1 = p9
if menor(p10, m1): m1 = p10
if menor(p11, m1): m1 = p11
if menor(p12, m1): m1 = p12
if menor(p13, m1): m1 = p13
if menor(p14, m1): m1 = p14
if menor(p15, m1): m1 = p15
if menor(p16, m1): m1 = p16
if menor(p17, m1): m1 = p17
if menor(p18, m1): m1 = p18
if menor(p19, m1): m1 = p19
if menor(p20, m1): m1 = p20

# Segundo menor
m2 = 999999
if (p1 == m1) == False and menor(p1, m2): m2 = p1
if (p2 == m1) == False and menor(p2, m2): m2 = p2
if (p3 == m1) == False and menor(p3, m2): m2 = p3
if (p4 == m1) == False and menor(p4, m2): m2 = p4
if (p5 == m1) == False and menor(p5, m2): m2 = p5
if (p6 == m1) == False and menor(p6, m2): m2 = p6
if (p7 == m1) == False and menor(p7, m2): m2 = p7
if (p8 == m1) == False and menor(p8, m2): m2 = p8
if (p9 == m1) == False and menor(p9, m2): m2 = p9
if (p10 == m1) == False and menor(p10, m2): m2 = p10
if (p11 == m1) == False and menor(p11, m2): m2 = p11
if (p12 == m1) == False and menor(p12, m2): m2 = p12
if (p13 == m1) == False and menor(p13, m2): m2 = p13
if (p14 == m1) == False and menor(p14, m2): m2 = p14
if (p15 == m1) == False and menor(p15, m2): m2 = p15
if (p16 == m1) == False and menor(p16, m2): m2 = p16
if (p17 == m1) == False and menor(p17, m2): m2 = p17
if (p18 == m1) == False and menor(p18, m2): m2 = p18
if (p19 == m1) == False and menor(p19, m2): m2 = p19
if (p20 == m1) == False and menor(p20, m2): m2 = p20

# Tercer menor
m3 = 999999
if (p1 == m1) == False and (p1 == m2) == False and menor(p1, m3): m3 = p1
if (p2 == m1) == False and (p2 == m2) == False and menor(p2, m3): m3 = p2
if (p3 == m1) == False and (p3 == m2) == False and menor(p3, m3): m3 = p3
if (p4 == m1) == False and (p4 == m2) == False and menor(p4, m3): m3 = p4
if (p5 == m1) == False and (p5 == m2) == False and menor(p5, m3): m3 = p5
if (p6 == m1) == False and (p6 == m2) == False and menor(p6, m3): m3 = p6
if (p7 == m1) == False and (p7 == m2) == False and menor(p7, m3): m3 = p7
if (p8 == m1) == False and (p8 == m2) == False and menor(p8, m3): m3 = p8
if (p9 == m1) == False and (p9 == m2) == False and menor(p9, m3): m3 = p9
if (p10 == m1) == False and (p10 == m2) == False and menor(p10, m3): m3 = p10
if (p11 == m1) == False and (p11 == m2) == False and menor(p11, m3): m3 = p11
if (p12 == m1) == False and (p12 == m2) == False and menor(p12, m3): m3 = p12
if (p13 == m1) == False and (p13 == m2) == False and menor(p13, m3): m3 = p13
if (p14 == m1) == False and (p14 == m2) == False and menor(p14, m3): m3 = p14
if (p15 == m1) == False and (p15 == m2) == False and menor(p15, m3): m3 = p15
if (p16 == m1) == False and (p16 == m2) == False and menor(p16, m3): m3 = p16
if (p17 == m1) == False and (p17 == m2) == False and menor(p17, m3): m3 = p17
if (p18 == m1) == False and (p18 == m2) == False and menor(p18, m3): m3 = p18
if (p19 == m1) == False and (p19 == m2) == False and menor(p19, m3): m3 = p19
if (p20 == m1) == False and (p20 == m2) == False and menor(p20, m3): m3 = p20

# Output
print("1er lugar (promedio más rápido):", m1)
print("2do lugar:", m2)
print("3er lugar:", m3)
