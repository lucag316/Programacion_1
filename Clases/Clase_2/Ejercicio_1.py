# EJERCICIO 1.	
# Un bar nos contrato para administrar el consumo de los clientes en las distintas mesas del local. Para esto debemos desarrollar un algoritmo que nos permita el ingreso de los siguientes datos:

# a.	Nombre del cliente
# b.	Tipo de bebida (validar cerveza, limonada, gaseosa, nada)
# c.	Tipo de comida (papitas, hamburguesa, rabas, nada)
	
# 	Los precios del bar son:
# 		Cerveza 500 $
# 		Limonada 300 $
# 		Gaseosa 250 $
# 		Papitas 1200 $
# 		Hamburguesa 2000 $
# 		Rabas 1800 $

# Luego de tomar los datos, se nos pide también realizar algunos datos estadísticos    con respecto a las consumiciones hechas durante la jornada de la cual no se sabe exactamente cuanta cantidad de ventas se han realizado, a saber se nos pide

# a.	El tipo de comida más vendido y bebida más vendida si la hay.
# b.	El promedio de clientes que ordena solamente bebida.
# c.	Calcular la recaudación bruta y recaudación neta del local.
# d.	Cuánta gente ordenó comida pero no bebida.

respuesta = "si"

cantidad_clientes = 0

tipo_comida_mas_vendida = ""
tipo_bebida_mas_vendida = ""

cantidad_bebida = 0
cantidad_comida = 0

cantidad_cerveza = 0
cantidad_limonada = 0
cantidad_gaseosa = 0

cantidad_papitas = 0
cantidad_hamburguesa = 0
cantidad_rabas = 0

cantidad_solo_bebida = 0


while respuesta == "si":

    nombre = input("Ingrese el nombre del cliente: ")

    bebida = input("Ingrese el tipo de bebida, [cerveza], [limonada], [gaseosa], [nada]: ")
    while(bebida != "cerveza" and bebida != "limonada" and bebida != "gaseosa" and bebida != "nada"):
        bebida = input("ERROR, vuelva a ingresar la bebida, [cerveza], [limonada], [gaseosa], [nada]: ")

    comida = input("Ingrese el tipo de comida, [papitas], [hamburguesa], [rabas], [nada]: ")
    while(comida != "papitas" and comida != "hamburguesa" and comida != "rabas" and comida != "nada"):
        comida = input("ERROR, vuelva a ingresar la comida, [papitas], [hamburguesa], [rabas], [nada]: ")

    if(bebida == "cerveza"):
        cantidad_cerveza += 1
    elif(bebida == "limonada"):
        cantidad_limonada += 1
    elif(bebida == "gaseosa"):
        cantidad_gaseosa += 1

    if(comida == "papitas"):
        cantidad_papitas += 1
    elif(comida == "hamburguesa"):
        cantidad_hamburguesa += 1
    elif(comida == "rabas"):
        cantidad_rabas += 1

    if (comida == "nada" and bebida != "nada"):
        cantidad_solo_bebida += 1
        
    cantidad_clientes += 1

    respuesta = input("Si quiere ingresar otro cliente presione [si]\nPara salir presione cualquier otra tecla\n")

cantidad_comida = cantidad_papitas + cantidad_hamburguesa + cantidad_rabas
cantidad_bebida = cantidad_cerveza + cantidad_limonada + cantidad_gaseosa

if (cantidad_comida > 0):
    if (cantidad_papitas > cantidad_hamburguesa and cantidad_papitas > cantidad_rabas):
        mensaje_comida = "Papitas"
    elif (cantidad_hamburguesa > cantidad_papitas and cantidad_hamburguesa > cantidad_rabas):
        mensaje_comida = "Hamburguesa"
    else:
        mensaje_comida = "Rabas"
else:
    mensaje_comida = "No se ordeno"

if (cantidad_bebida > 0): 
    if (cantidad_cerveza > cantidad_limonada and cantidad_cerveza > cantidad_gaseosa):
        mensaje_bebida = "Cerveza"
    elif (cantidad_limonada > cantidad_cerveza and cantidad_limonada > cantidad_gaseosa):
        mensaje_bebida = "limonada"
    else:
        mensaje_bebida = "Gaseosa"
else:
    mensaje_bebida = "No se ordeno"

    
if (cantidad_solo_bebida == 0):
    promedio_solo_bebida = "No hay"
else:
    promedio_solo_bebida = cantidad_clientes / cantidad_solo_bebida

print("Comida mas vendida: {0} \nBebida mas vendida: {1}".format(mensaje_comida, mensaje_bebida))
print("El promedio que solo ordena bebida: {0}".format(promedio_solo_bebida))

# b.	El promedio de clientes que ordena solamente bebida.
# c.	Calcular la recaudación bruta y recaudación neta del local.
# d.	Cuánta gente ordenó comida pero no bebida.