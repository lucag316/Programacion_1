# EJERCICIO 1 CLASE 3
# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de
# una compra de productos de prevención de contagio, de cada una debe obtener los
# siguientes datos:
# · El tipo ("barbijo", "jabón" o "alcohol")
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de
# stock.


respuesta = "si"
while respuesta == "si":
    tipo = input("Ingrese el tipo de producto [barbijo], [jabon] o [alcohol]: ")
    while tipo != "barbijo" and tipo != "jabon"  and tipo != "alcohol":
        tipo = input("ERROR, reingrese el tipo de producto [barbijo], [jabon] o [alcohol]: ")
    while True:
        try: 
            precio = float(input("Ingrese el precio del producto: ")) 
            if precio < 0:
                precio = float(input("ERROR, reingrese el precio del producto: "))
            else:
                break
        except ValueError:
            print("ERROR, solo puede ingresar numeros")
            
    while True:
        try:
            cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
            if cantidad_unidades < 0:
                cantidad_unidades = int(input("ERROR, reingrese la cantidad de unidades: "))
            else:
                break
        except ValueError:
            print("ERROR, solo puede ingresar numeros")

    marca = input("Ingrese la marca del producto: ")
    while marca == "":
        marca = input("ERROR, reingrese la marca del producto: ")
    
    fabricante = input("Ingrese el fabricante del producto: ")
    while fabricante == "":
        fabricante = input("ERROR, reingrese el fabricante del producto: ")
    print("\n=========================================================================================")
    print("Tipo: {0} \nPrecio: {1} \nCantidad de unidades {2} \nMarca: {3} \nFabricante: {4}".format(tipo, precio, cantidad_unidades, marca, fabricante)) # NO SE DONDE QUIERE EL PRINT
    print("=========================================================================================\n")
    respuesta = input("\n[si] para ingresar otro producto \n[otra tecla] para salir \n")



# respuesta = "si"
# while respuesta == "si":
#     tipo = input("Ingrese el tipo de producto [barbijo], [jabon] o [alcohol]: ")
#     while tipo != "barbijo" and tipo != "jabon"  and tipo != "alcohol":
#         tipo = input("ERROR, reingrese el tipo de producto [barbijo], [jabon] o [alcohol]: ")
        
#     precio = float(input("Ingrese el precio del producto: ")) 
#     while precio < 0:
#         precio = float(input("ERROR, reingrese el precio del producto: "))

#     cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
#     while cantidad_unidades < 0:
#         cantidad_unidades = int(input("ERROR, reingrese la cantidad de unidades: "))

#     marca = input("Ingrese la marca del producto: ")
#     while marca == "":
#         marca = input("ERROR, reingrese la marca del producto: ")
    
#     fabricante = input("Ingrese el fabricante del producto: ")
#     while fabricante == "":
#         fabricante = input("ERROR, reingrese el fabricante del producto: ")

#     print("Tipo: {0} \nPrecio: {1} \nCantidad de unidades {2} \nMarca: {3} \nFabricante: {4}".format(tipo, precio, cantidad_unidades, marca, fabricante)) # NO SE DONDE QUIERE EL PRINT

#     respuesta = input("\n[si] para ingresar otro producto \n[otra tecla] para salir \n")


