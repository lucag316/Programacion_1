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



while respuesta == "si":

    nombre = input("Ingrese el nombre del cliente: ")

    bebida = input("Ingrese el tipo de bebida, [cerveza], [limonada], [gaseosa], [nada]: ")
    while(bebida != "cerveza" and bebida != "limonada" and bebida != "gaseosa" and bebida != ""):
        bebida = input("ERROR, vuelva a ingresar la bebida, [cerveza], [limonada], [gaseosa], [nada]: ")

    comida = input("Ingrese el tipo de comida, [papitas], [hamburguesa], [rabas], [nada]: ")
    while(comida != "papitas" and comida != "hamburguesa" and comida != "rabas" and comida != ""):
        comida = input("ERROR, vuelva a ingresar la comida, [papitas], [hamburguesa], [rabas], [nada]: ")

    if(bebida == "cerveza"):
        cantidad_cerveza += 1
    elif(bebida == "limonada"):
        cantidad_limonada += 1
    else:
        cantidad_gaseosa += 1

    if(comida == "papitas"):
        cantidad_papitas += 1
    elif(comida == "hamburguesa"):
        cantidad_hamburguesa += 1
    else:
        cantidad_rabas += 1

    if(ca):

    respuesta = input("Si quiere ingresar otro cliente presione [si]\nPara salir presione cualquier otra tecla\n")

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