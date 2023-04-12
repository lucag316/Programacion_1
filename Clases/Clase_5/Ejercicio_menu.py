# Ejercicio con Menú de Opciones
# Realizar un programa utilizando los conceptos de la clase del lunes:
# Opciones del menú:
# # 1 cargar una lista con 10 números
# # 2 mostrar el total de los números ingresados
# # 3 mostrar el promedio
# # 4 mayor
# # 5 menor
# # 6 pedir un número y decir si está en la lista
# # 7 pedir un número e informar todos los índices donde aparece
# # 8 informar cuantos números pares y cuantos impares hay en la lista
# #9 informar cuantos positivos, cuantos negativos y cuantos ceros hay en la lista
# # 10 vaciar lista
# #11 Salir
# Para utilizar las opciones 2 a la 10 hay que cargar los números en la opción 1
# Si se vacía la lista con la opción 10 se deben bloquear nuevamente las opciones hasta que se
# cargue de nuevo los números con la opción 1


lista_numeros = [5, 0, 50, -60, 7, 10, -99, 85, 74, 0]

acumulador_numeros = 0
cantidad_numeros = 0
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

menor = lista_numeros[0]
mayor = lista_numeros[0]



numero_ingresado = int(input("Ingrese un numero: "))
# print(f"indices en los que aparece {indice}")
# indice = lista_numeros.index(numero)
for numero in lista_numeros:
    if numero_ingresado == numero:
        print("el numero si esta en la lista")
        indice = lista_numeros.index(numero)
        print(f"indices en los que aparece {indice}")

for numero in lista_numeros:
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
        
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1

for numero in lista_numeros:
    acumulador_numeros += numero
    cantidad_numeros = len(lista_numeros)
    
    if numero > mayor:
        mayor = numero
        
    if numero < menor:
        menor = numero

promedio_numeros = acumulador_numeros / cantidad_numeros
# # 7 pedir un número e informar todos los índices donde aparece
# # 10 vaciar lista
lista_vacia = lista_numeros.clear()
print(acumulador_numeros)
print(promedio_numeros)
print(mayor)
print(menor)
print(f"pares {contador_pares}    |   impares: {contador_impares}")
print(f"positivos: {contador_positivos}  | negativos: {contador_negativos}    | ceros: {contador_ceros}")
print(f"lista vacia: {lista}")






# lista_numeros = []
# acumulador_numeros = 0
# contador_numeros = 0

# bandera_mayor = False
# bandera_menor = True

# for i in range(3):
#     numero_ingresado = int(input("Ingrese un numero: "))
#     lista_numeros.append(numero_ingresado)
    
#     if numero_ingresado i

# for numero in lista_numeros:
#     acumulador_numeros += numero
#     contador_numeros += 1
    
#     if bandera_mayor == False or numero > mayor:
#         mayor = numero
#         bandera_mayor = True
        
#     if bandera_menor == False or numero < menor:
#         menor = numero
#         bandera_menor = True
    
# promedio_numeros = acumulador_numeros / contador_numeros
# # # 6 pedir un número y decir si está en la lista
# print(acumulador_numeros)
# print(promedio_numeros)
# print(mayor)
# print(menor)