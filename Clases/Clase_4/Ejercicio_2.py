# EJERCICIO 2 CLASE 4

# La real academia española nos pide desarrollar un pequeño programa que contenta el
# diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
# algoritmo que nos permita el ingreso de una palabra en español y su traducción al
# ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
# palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
# esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
# debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
# inglés. Recordar validar los datos de forma correcta.

lista_palabras = []
#lista_palabras_ingles = []
bandera_palabra = False

respuesta = "si"
while respuesta == "si":
    palabra_español = input("ingrese una palabra: ")
    
    for palabra in lista_palabras:
        if palabra == palabra_español:
            bandera_palabra = True

    if bandera_palabra:
        indice = lista_palabras.index(palabra_español)
        print(f"ya esta en la lista en el indice: {indice}")
        bandera_palabra = False
    else:
        #print("no esta")
        lista_palabras.append(palabra_español)
        traduccion = input("Ingrese su traduccion: ")
        lista_palabras.append(traduccion)
    
    respuesta = input("[si] para continuar \n[otra tecla] para salir\n")

print(lista_palabras)
# lista_palabras.extend(lista_palabras_ingles)

# print(lista_palabras)

