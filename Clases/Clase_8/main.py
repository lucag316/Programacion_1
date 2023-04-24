from data_stark import lista_personajes

lista = []
colores = []

for heroe in lista_personajes:
    lista.append(heroe.copy())
    for clave in heroe:
        color = clave["color_ojos"]
        if color not in colores:
            colores.append(color)
            
            
for heroe in lista_personajes:
    lista.append(heroe.copy())
    
for heroe in lista:
    colores.append(clave["color_ojos"])