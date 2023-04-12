from data import personas

# bandera = True
# edad_mayor = None # funciona igual sin esto, pero queda mejor
# for persona in personas:
#     if bandera or persona["edad"] > edad_mayor:
#         edad_mayor = persona["edad"]
#         persona_mayor = persona
#         bandera = False

# print(f"edad mayor: {edad_mayor}\npersona mayor: {persona_mayor}")
persona_mayor = personas[0]

for persona in personas:
    if persona["edad"] > persona_mayor["edad"]:
        persona_mayor = persona

#print(f"la persona mayor es: {persona_mayor}")

for persona in personas:
    if persona["edad"] == persona_mayor["edad"]:
        print(persona)