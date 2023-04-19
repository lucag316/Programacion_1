# ERJERCICIO CON MENU DE OPCIONES

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
import os

lista_numeros = []
lista_indices = []

acumulador_numeros = 0
cantidad_numeros = 0
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

bandera_numero = False
bandera_numeros_cargados = False

while True:
    os.system("cls")
    print("***MENU DE OPCIONES***")
    print("-----------------------")
    print("1- Carga una lista con 10 numeros \n2- Muestra el total de los numeros ingresados \n3- Muestra el promedio \n4- Muestra el numero mayor \n5- Muestra el numero menor \n6- Pide un numero y dice si esta en la lista \n7- Pide un numero e informa todos los índices donde aparece \n8- Informa cuantos numeros pares e impares hay en la lista \n9- Informa cuantos positivos, negativos y veros hay en la lista \n10- Vacia la lista \n11- Salir")
    
    opcion = int(input("Elija una opcion: "))
    
    if opcion == 1:
        bandera_numeros_cargados = True
        for i in range(3):
            numero_appendeado= int(input("Ingrese un numero a la lista: "))
            lista_numeros.append(numero_appendeado)
    elif opcion == 2:
        if bandera_numeros_cargados:
            for numero in lista_numeros:
                acumulador_numeros += numero
            print(f"El total es: {acumulador_numeros}")
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 3:
        if bandera_numeros_cargados:
            cantidad_numeros = len(lista_numeros)
            promedio_numeros = acumulador_numeros / cantidad_numeros
            print(f"El promedio es: {promedio_numeros}")
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 4:
        if bandera_numeros_cargados:
            mayor = lista_numeros[0]
            for numero in lista_numeros:
                if numero > mayor:
                    mayor = numero
            print(f"El numero mas grande es: {mayor}")
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 5:
        if bandera_numeros_cargados:
            menor = lista_numeros[0]
            for numero in lista_numeros:
                if numero < menor:
                    menor = numero
            print(f"El numero mas chico es: {menor}")
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 6:
        if bandera_numeros_cargados:
            numero_ingresado = int(input("Ingrese un numero: "))
            for numero in lista_numeros:
                if numero_ingresado == numero:
                    bandera_numero = True
                        #break      NO SE SI VA
            if bandera_numero:
                print("el numero SI esta en la lista") 
            else:
                print("el numero NO esta en la lista")
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 7:
        if bandera_numeros_cargados:
            numero_ingresado = int(input("Ingrese un numero: "))
            for numero in lista_numeros:
    
                #cantidad = lista_numeros.count(numero_ingresado)
                # if  cantidad > 1:
                #     print("el numero si esta en la lista")
                #     break
    
                #indice = lista_numeros.index(numero_ingresado)
                #print(f"indices en los que aparece: {indice}") # TIENE QUE APARECER MAS DE 1 INDICE
                if numero_ingresado == numero:
                    indice = lista_numeros.index(numero)
                    lista_indices.append(indice)            # EL PUNTO 7, LO DEL  INDICE ESTA MAL HECHO
            print(f"Indices en los que aparece: {lista_indices}")
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 8:
        if bandera_numeros_cargados:
            for numero in lista_numeros:
                if numero % 2 == 0:
                    contador_pares += 1
                else:
                    contador_impares += 1
            print(f"hay {contador_pares} pares y {contador_impares} impares")
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 9:
        if bandera_numeros_cargados:
            for numero in lista_numeros:
                if numero > 0:
                    contador_positivos += 1
                elif numero < 0:
                    contador_negativos += 1
                else:
                    contador_ceros += 1
            print(f"hay {contador_positivos} positivos, {contador_negativos} negativos y {contador_ceros} ceros")
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 10:
        if bandera_numeros_cargados:
            lista_numeros.clear()
            bandera_numeros_cargados = False
        else:
            print("Primero debes cargar los numeros en la opcion 1")
    elif opcion == 11:
        salir = input("[s] para salir \n[otra tecla] para cancelar\n")
        if salir == "s":
            break
    os.system("pause")

















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