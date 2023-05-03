import re

frase = "Esto es un texto de prueba para practicar expresiones regulares"

parte = re.compile("texto")

variable = parte.findall(frase)
variable_2 = re.findall("texto", frase)



print(variable)
print(variable_2)

print("----------------------------------")






