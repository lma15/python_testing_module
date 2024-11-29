"""
Ultima Modificación: 29/11/2024
Autor. Leandro Morales Aranda
"""
import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es un palíndromo.
    Ignora espacios, mayúsculas y tildes.
    """
    def normalizar(texto):
        # Normaliza el texto eliminando acentos y convirtiendo a minúsculas
        texto = unicodedata.normalize('NFD', texto)
        texto = ''.join(char for char in texto if unicodedata.category(char) != 'Mn')
        return texto.lower()

    # Normalizar la cadena
    cadena_normalizada = normalizar(cadena)

    # Filtrar solo caracteres alfanuméricos
    cadena_filtrada = ''.join(char for char in cadena_normalizada if char.isalnum())

    # Comprobar si es un palíndromo
    return cadena_filtrada == cadena_filtrada[::-1]


