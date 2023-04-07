# EJERCICIO 1 CLASE 4

# Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
# autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
# marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
# listas primero, y despues usando listas y comparar la composición del código.


respuesta = "si"

while respuesta == "si":
    
    marca = input("\nIngrese la marca del auto: ")
    while marca == "":
        marca = input("ERROR, reingrese la marca del auto: ")
    
    año_modelo = int(input("Ingrese el año del modelo: "))
    while año_modelo < 1900 or año_modelo > 2023:
        año_modelo = int(input("ERROR, reingrese el año del modelo: "))
    
    precio = float(input("Ingrese el precio del auto: "))
    while precio < 0:
        precio = float(input("ERROR, reingrese el precio del auto: "))
    
    respuesta = input("[si] para continuar \n[otra tecla] para salir\n")
    print("Marca: {0} \nAño del modelo: {1} \nPrecio ${2}\n".format(marca, año_modelo, precio))
    
    
    
    