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

lista_numeros = []
acumulador_numeros = 0
contador_numeros = 0

bandera_mayor = False
bandera_menor = True

for i in range(3):
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_numeros.append(numero_ingresado)
    
    if numero_ingresado i

for numero in lista_numeros:
    acumulador_numeros += numero
    contador_numeros += 1
    
    if bandera_mayor == False or numero > mayor:
        mayor = numero
        bandera_mayor = True
        
    if bandera_menor == False or numero < menor:
        menor = numero
        bandera_menor = True
    
promedio_numeros = acumulador_numeros / contador_numeros
# # 6 pedir un número y decir si está en la lista
print(acumulador_numeros)
print(promedio_numeros)
print(mayor)
print(menor)