""" 
Ultima Modificación: 29/11/2024 
Autor: Leandro Morales Aranda
"""

import unittest
from app.scripts.charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):

    # Pruebas para cadenas palíndromas
    def test_cadenas_palindromas(self):
        self.assertTrue(esPalindromo("anilina"))
        self.assertTrue(esPalindromo("aibohphobia"))
        self.assertTrue(esPalindromo("radar"))
        self.assertTrue(esPalindromo("reconocer")) 
        self.assertTrue(esPalindromo("salas")) 

    # Pruebas para cadenas que no son palíndromas
    def test_cadenas_no_palindromas(self):
        self.assertFalse(esPalindromo("palabra"))
        self.assertFalse(esPalindromo("python"))
        self.assertFalse(esPalindromo("programar"))
        self.assertFalse(esPalindromo("ejemplo")) 

    # Pruebas para cadenas con caracteres diversos, incluyendo espacios y puntuación
    def test_caracteres_varios(self):
        self.assertTrue(esPalindromo("A man, a plan, a canal, Panama"))
        self.assertTrue(esPalindromo("No 'x' in Nixon"))
        self.assertTrue(esPalindromo("La ruta natural")) 
        self.assertFalse(esPalindromo("Esto no es un palindromo"))

    # Pruebas para cadenas con combinación de mayúsculas y minúsculas
    def test_mayusculas_minusculas(self):
        self.assertTrue(esPalindromo("Anilina"))
        self.assertTrue(esPalindromo("RaCeCar"))
        self.assertTrue(esPalindromo("Somos")) 
        self.assertFalse(esPalindromo("Python"))

    # Pruebas para cadenas vacías
    def test_cadenas_vacias(self):
        self.assertTrue(esPalindromo(""))  # Una cadena vacía es técnicamente un palíndromo

if __name__ == "__main__":
    unittest.main()