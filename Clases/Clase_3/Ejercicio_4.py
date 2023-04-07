# EJERCICIO 4 CLASE 3
# La división de alimentos está trabajando en un pequeño software para cargar las
# compras de ingredientes para la cocina de Industrias Wayne.
# Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
# para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
# de ingredientes.
# Se registra por cada compra:
# 1. PESO: (entre 10 y 100 kilos)
# 2. PRECIO POR KILO: (mayor a 0 [cero]).
# 3. TIPO VARIEDAD: (vegetal, animal, mezcla).
# Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
# descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
# de descuento sobre el precio bruto.
# Se desea saber:
# A. El importe total a pagar, BRUTO sin descuento.
# B. El importe total a pagar con descuento (Solo si corresponde).
# C. Informar el tipo de alimento más caro.
# D. El promedio de precio por kilo en total.

acumulador_peso = 0

for compra in range(3):                                     #SON 15
    peso = float(input("Ingrese el peso [entre 10 y 100 kilos]: "))
    while peso < 10 or peso > 100:
        peso = float(input("ERROR, reingrese el peso [entre 10 y 100 kilos]: "))
    
    precio_kilo = float(input("Ingrese el precio por kilo: "))
    while precio_kilo < 0:
        precio_kilo = float(input("ERROR reingrese el precio por kilo: "))
    
    tipo = input("Ingrese el tipo [vegetal], [animal], [mezcla]: ")
    while tipo != "vegetal" and tipo != "animal" and tipo != "mezcla":
        tipo = input("ERROR, reingrese el tipo [vegetal], [animal], [mezcla]: ")
    
    acumulador_peso += peso

if acumulador_peso > 100:
    precio_total = acumulador_peso * 0.85

# Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
# descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
# de descuento sobre el precio bruto.
# Se desea saber:
# A. El importe total a pagar, BRUTO sin descuento.
# B. El importe total a pagar con descuento (Solo si corresponde).
# C. Informar el tipo de alimento más caro.
# D. El promedio de precio por kilo en total.