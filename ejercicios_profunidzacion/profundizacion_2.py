# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

inicio = int(input('Ingrese el primer número a calcular\n'))
fin = int(input('Ingrese el segundo número a calcular\n'))
simbolo = str(input("Ingresar el simbolo a operar"))

while True:
   
    if simbolo == "+":
        sumar = (inicio + fin)
        print("La suma es:", sumar)
    elif simbolo == "-":
          restar = (inicio - fin)
        print("La resta es:", restar)
    elif simbolo == "*":
        multiplicacion = (inicio * fin)
        print("La multiplicacion es:", multiplicacion)
    elif simbolo == "/":
        division = (inicio / fin)
        print("La division es", division)
    elif simbolo == "**":
        potencia = (inicio ** fin)
        print("La potencia es:", potencia)
    else:
       print("Error")
    if simbolo == "FIN":
        print("Se apaga la calculadora")
        break