"""
Incluye funciones para contar el número de sílabas,
de palabras y de oraciones contenidas en un texto
que se recibe como entrada.
"""

def contar_oraciones(texto):
    """Cuenta y devuelve el número de oraciones en texto."""
    signos_puntuacion = ['.', '?', '!', ':', ';']
    oraciones = 0
    
    for caracter in texto:
        if caracter in signos_puntuacion:
            oraciones += 1

    # Al menos 1 oración si no hay signos
    return oraciones if oraciones > 0 else 1  
    

def contar_palabras(texto):
    """Cuenta y devuelve el número de palabras en texto."""
    palabras = texto.split()
    return len(palabras)


def contar_silabas(texto):
    """Cuenta y devuelve el número de sílabas en texto."""
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    silabas = 0
    
    for caracter in texto:
        if caracter in vocales:
            silabas += 1

    # Al menos 1 sílaba por palabra
    return silabas if silabas > 0 else 1 
