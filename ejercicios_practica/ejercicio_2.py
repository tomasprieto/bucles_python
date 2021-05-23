# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores
colores = ['rojo', 'naranja', 'verde', 'azul']

# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...

# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...



for color in colores:
    print(color)


for x in colores[0]:
    print(x)
for x in colores[1]:
    print(x)
for x in colores[2]:
    print(x)
for x in colores[3]:
    print(x)

lista_color = len(colores)

for i in range(lista_color):
    print("El índice",i," color:", colores[i])

print("terminamos!")