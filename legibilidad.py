"""
Funciones para calcular el índice de Velázquez Gaytán (utilizando el módulo analisis_texto) 
y para decidir el nivel de legibilidad de un texto.
"""


from analisis_texto import contar_oraciones, contar_palabras, contar_silabas

def indice_legibilidad_VG(texto):
    """Calcula y devuelve el índice de Velázquez Gaytán del texto de entrada."""
    # Ahora uso las funciones directamente
    oraciones = contar_oraciones(texto) 
    palabras = contar_palabras(texto)
    silabas = contar_silabas(texto)
    
    # Evitar división por cero
    if oraciones == 0:
        oraciones = 1
    if palabras == 0:
        palabras = 1
    
    L = 206.84 - 1.02 * (palabras / oraciones) - 60 * (silabas / palabras)
    
    # Asegurar que el índice esté entre 0 y 100
    L = max(0, min(100, L))
    
    return oraciones, palabras, silabas, round(L, 2)

def nivel_legibilidad_VG(indice):
    """Decide y devuelve el nivel de legibilidad de un texto de acuerdo con el índice de Velázquez Gaytán."""
    if indice >= 90:
        return "Muy fácil"
    elif indice >= 80:
        return "Fácil"
    elif indice >= 70:
        return "Relativamente fácil"
    elif indice >= 60:
        return "Normal"
    elif indice >= 50:
        return "Relativamente difícil"
    elif indice >= 30:
        return "Difícil"
    else:
        return "Muy difícil"
