from data_stark import lista_personajes
"""
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
"""
lista_personajes_nueva = []
for heroe in lista_personajes:
    lista_personajes_nueva.append(heroe.copy())
#---------------------------------------------------------------------1.1
def extraer_iniciales(nombre_heroe: str) -> str:
    """
    Brief: Se le pasa por parametro un nombre, se extraen las iniciales y se le agrega un punto, si el nombre contiene "the", se omite, solo si contiene guion se le reemplaza por un espacio, se valida que no este vacio el  string recibido
    
    Parameters:
        nombre_heroe: str -> El nombre del heroe que se le  extraeran las iniciales
    
    Return: Devuelve un nuevo string con las iniciales del nombre seguido de puntos, en caso de no cumplirse la validacion devuelve "N/A"
    """
    retorno = "N/A"
    iniciales = ""
    if(nombre_heroe != ""):
        nombre_heroe = nombre_heroe.upper()
        if "-" in nombre_heroe:
            nombre_heroe = nombre_heroe.replace("-", " ")
        if "THE" in nombre_heroe:
            nombre_heroe = nombre_heroe.replace("THE", "")
            
        nombre_heroe = nombre_heroe.strip()
        partes = nombre_heroe.split(" ")
        
        for parte in partes:
            iniciales += parte[0]+ "."
        retorno = iniciales

    return retorno


print(extraer_iniciales("HOward The ducK"))