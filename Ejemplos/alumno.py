lista_notas_1 = []
lista_notas_2 = []
promedios = []

for i in range(2):
    nota_1 = int(input("Ingrese la primer nota: "))
    lista_notas_1.append(nota_1)

    nota_2 = int(input("Ingrese la segunda nota: "))
    lista_notas_2.append(nota_2)

    promedio = (lista_notas_1[i] + lista_notas_2[i]) / 2
    promedios.append(promedio)

print("Nota 1       Nota 2      promedio")
for i in range(len(lista_notas_1)):
    print(f"  {lista_notas_1[i]:2d}          {lista_notas_2[i]:2d}          {promedios[i]:5.2f}") 

#  El 2f es la cantidad de numeros que quiero despues de la coma (2 decimales, osea 2 numeros despues del punto)(el 5 es, que quiero que tanga un ancho de 5)
# El 2d, le estoy diciendo, mostramelo con 2 cifras (2 enteros)
# pondria 02d si quiero que aparezca por ejemplo asi 04

# PODRIA AGREGAR LISTAS DE LEGAJOS O NOMBRE O ALGO
