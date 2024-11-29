""" 
Ultima Modificación: 29/11/2024 
Autor: Leandro Morales Aranda
"""

from charfun import esPalindromo

def main():
    """
    Función principal que solicita al usuario introducir frases para verificar si son palíndromas.
    El programa finaliza cuando el usuario escribe 'salir'.
    """
    while True:
        # Solicitar entrada al usuario
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")

        # Comprobar si el usuario desea salir
        if frase.lower() == "salir":
            print("Programa finalizado.")
            break
        else:
            # Verificar si la frase es un palíndromo
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")

# Ejecutar el programa si el script se ejecuta directamente
if __name__ == "__main__":
    main()