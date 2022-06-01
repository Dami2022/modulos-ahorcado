import random
from palabras import *


def obtener_palabra_valida(pal):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()