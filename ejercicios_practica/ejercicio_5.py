# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior




inicio = int(input('Ingrese el primero número de la secuencia\n'))
fin = int(input('Ingrese el ultimo número de la secuencia\n'))
# fin....
suma = 0
for i in range(inicio, fin + 1):
    print("Vuelta numero", (i - inicio + 1), "del bucle")
    print("Numero de la secuencia:", i)
    suma = suma + i
    print("Suma parcial es:", suma)
# Imprimir el valor de la sumatoria
print("La suma total es", suma)
print("terminamos!")