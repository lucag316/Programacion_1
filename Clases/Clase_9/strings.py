cadena = "esto es una cadena"
#print(cadena[0])
print(cadena.capitalize())
print(cadena.lower())
print(cadena.upper())
#cadena.index()
print(cadena.count("e"))

print("hola mundo".upper())

cadena = cadena.capitalize()
print(cadena)






cadena_nueva = "esTo eS UNa caDeNa"
aux = list(cadena_nueva)

# for caracter in aux:
#     if caracter.:

for i in range(len(aux)):  # uso el indice
    if aux[i].islower():
        aux[i] = aux[i].upper() # podria hacer directo  esto, pero es mejor agregarle el if de arriba

print(aux)
print("".join(aux))  # une todo el iterable en un string

print("----------------------------------------------")

cadena_3 = "    Esto es una cadena    "

print(cadena_3)
print(cadena_3.strip())

cadena_4 = "   Esto es una cadena00000"
print(cadena_4)
print(cadena_4.strip("0"))
print("-----")
cadena_4 = "   Esto es una cadena00000 "
print(cadena_4)
print(cadena_4.strip("0")) # hay un espacio al final entonces no lo corta



# islower()          devuelve True si todos los caracteres que esta en la  cadena estan en minuscula
# isupper()          lo mismo pero mayuscula
# strip()             saca los espacios del principio y del final(en los limites)(se puede poner varios, ej variable.strip().strip("0"))

# and, not, or, in    son operradores logicos
# +, -, *, /, %       son operadores aritmeticos
# >, <, >=, <=, ==, != son operadores relacionales


# los relacionales tiene mas prioridad que los logicos


# LAS CADENAS CON INMUTABLES
# SALVO LOS SETS, LISTA Y DICCIONARIOS, TODOS SON INMUTABLES