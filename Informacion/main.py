# shift + alt + f                  ordena el codigo(las tabulaciones y eso)
#control + llave de cierre         para comentar todas las lineas















#---------------------------------------LISTAS---------------------------------------------------------------
# append                          agrega al elemento en la ultima posicion
# insert                          lo agrega  en el indice que quieras
# extend                          une la lista a la otra, al final
# remove                          elimina al elemento de la lista
# pop                             remueve el elemento de la lista y lo retorna (si no le paso nada, remueve el ultimo)
# reverse                         invierte la lista
# sort                            ordena la lista
# sort(reverse = True)            la  ordena al  reves
# index                           retorna el indice
# clear                           deja vacia la lista
# count                           me devuelve la cantidad de veces que este un valor
#---------------------------------------LISTAS---------------------------------------------------------------


#---------------------------------------DICCIONARIOS---------------------------------------------------------
# del                             ej: del alumno["edad"]     elimina la clave edad del alumno
# variable.keys()                 me devuelve un elemento de tipo "claves de dic" donde tengo todas las claves
#se puede hacer --> for key in variable.keys:
# variable.values()               este metodo me devuelve un elemento dict values (te devuelve una lista con los valores)(parecido al de keys)
# alumno.get("nombre")            accede al valor, lo mismo que alumno["nombre"]
#
#---------------------------------------DICCIONARIOS---------------------------------------------------------









# import data                      despues tengo que poner por ejemplo   data.personas
# from data import personas        no hace falta  el punto (solo traigo a "personas")
# from data import personas, numeros  se puede pero solo si data y el main por ejemplo, esta en la misma carpeta
# from data import *               traigo todo



# La diferencia entre funcion y metodo es que cuando una funcion esta dentro de un objeto, en vez de llamarse funcion, se llama metodo. Si la funcion esta sola, se le dice funcion (conceptualmente es lo mismo, un algoritmo o bloque de codigo que le pusieron una etiqueta).









#---------------------------------------STRINGS---------------------------------------------------------
# son inmutables(no modifican el string original, sino que me devuelven uno nuevo), cada variable tiene su metodo, aunque no lo tenga en una variable, on the fly se puede pero no se guarda, 
# 

# cadena.lower()                tengo que guardarlo en una variable porque si despues pongo print(cadena) sigue  estando como antes
# cadena.upper()
# caracter.islower()            me devuelve un booleano, true si todos estan en minuscula
# cadena.isupper()                                                              mayuscula
# cadena.isalpha()                                                              son caracteres alfabeticos
# cadena.isalnum()                                                                             alfanumeriticos
# cadena.join()                 me devuelve una cadena contatenando todos los elementos del nuevo
# cadena.strip()                saca todo los espacios de los costados, si le paso algo por parametro, saca todo lo que le pasamos, ej si pongo cadena.strip("0") saca todos los ceros de los costados
# cadena.split(" ")            separa(corta) toda la cadena por el parametro que le pases, ej aca por los espacios, lo hace lista
# cadena.replace("algo", "por esto")    remplaza el primer parametro por lo del otro parametro
# cadena.zfill(numero)          rellena la cadena con ceros a la izquierda 
# cadena.count("algo")          me devuelve un int, cuenta la cantidad de ocurrencias de "algo"
# cadena[numero:numero]     -> slice            corta una rebanada de la cadena, el primer numero es donde empieza(inclusivo), el segundo donde termina(exclusivo)
# 
# 
#---------------------------------------STRINGS---------------------------------------------------------






# corregir algo y volverlo a guardar





