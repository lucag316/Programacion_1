# EJERCICIO 2
# Una librería que se especializa en venta de libros importados desea calcular ciertas métricas en base
# a las ventas de sus productos.
# Se ingresa de cada venta:
# Título del libro
# Género: (ciencia ficción – Drama – Terror)
# Material del libro (rústica – tapa dura)
# Importe (No pueden ser números negativos ni mayor a los 30000)
# Se pide:                          	
# a) El libro más barato de drama con su importe.
# b) Del libro más caro, el título.
# c) Porcentaje de libros de cada género
# d) La cantidad de libros que sean de ciencia ficción y cuesten menos de $700.
# e) cantidad de libros de ciencia ficcion o drama que cuesten mas de $500.

respuesta = "si"

bandera_drama_mas_barato = False
#drama_mas_barato = 10000000000            #HABIA UNA FORMA MEJOR
#importe_drama_mas_barato = None  CREO QUE NO VA
#titulo_drama_mas_barato = ""    CREO QUE NO VA

#titulo_mas_caro = ""            CREO QUE NO VA
bandera_mas_caro = False
importe_mas_caro = 0               #HABIA UNA FORMA MEJOR

cantidad_libros = 0
cantidad_ciencia_ficcion = 0
cantidad_drama = 0
cantidad_terror = 0

cantidad_ciencia_ficcion_menor_700 = 0
cantidad_drama_ficcion_mas_500 = 0
while respuesta == "si":

    titulo = input("Ingrese el titulo del libro: ")

    genero = input("Ingrese el genero del libro [ciencia ficcion], [drama], [terror]: ")
    while genero != "ciencia ficcion" and genero != "drama" and genero != "terror":
        genero = input("ERROR, reingrese el genero [ciencia ficcion], [drama], [terror]: ")

    material = input("Ingrese el material del libro [rustica], [tapa dura]: ")
    while material  != "rustica" and material != "tapa dura":
        material = input("ERROR, reingrese el material [rustica], [tapa dura]: ")
    
    importe = int(input("Ingrese su importe [entre 0 y 30000]: "))
    while importe < 0 or importe > 30000:
        importe = int(input("ERROR, reingrese su importe [entre 0 y 30000]: "))


    if importe > importe_mas_caro or bandera_mas_caro == False:

        importe_mas_caro = importe
        titulo_mas_caro = titulo
        bandera_mas_caro = True

    if genero == "ciencia ficcion":
        cantidad_ciencia_ficcion += 1
        if importe < 700:
            cantidad_ciencia_ficcion_menor_700 += 1

    elif genero == "drama":
        cantidad_drama += 1
        if importe < importe_drama_mas_barato or bandera_drama_mas_barato == False: 
            titulo_drama_mas_barato = titulo
            importe_drama_mas_barato = importe
            bandera_drama_mas_barato = True

    else:
        cantidad_terror += 1
    
    if genero == "ciencia ficcion" or genero == "drama" and importe > 500:
        cantidad_drama_ficcion_mas_500 += 1

    cantidad_libros += 1

    respuesta = input("[si] PARA CONTINUAR\n[otra tecla] PARA SALIR:\n")

porcentaje_ciencia_ficcion = (cantidad_ciencia_ficcion * 100) / cantidad_libros
porcentaje_drama = (cantidad_drama * 100) / cantidad_libros
porcentaje_terror = (cantidad_terror * 100) / cantidad_libros

#----------------------------------------------OUTPUT------------------------------------------------------------
print("El libro mas barato de drama es: {0} con un importe de: {1}".format(titulo_drama_mas_barato, importe_drama_mas_barato))
print("El libro mas caro es: {0}".format(titulo_mas_caro))
print("El porcentaje de libros de cada genero es: {0} de Ciencia Ficcion, {1} de Drama y {2} de Terror".format(porcentaje_ciencia_ficcion, porcentaje_drama, porcentaje_terror))
print("La cantidad de libros de ciencia ficcion menor a $700 es: {0}". format(cantidad_ciencia_ficcion_menor_700))
print("La cantidad de libros de ciencia ficcion o drama mayores a $500 es: {0}".format(cantidad_drama_ficcion_mas_500))
#----------------------------------------------OUTPUT------------------------------------------------------------
