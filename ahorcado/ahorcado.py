import random
import string
from ahorcado_diagrama import diccionario_vidas
from palabra_valida import *

def ahorcado():
    print("**********************************")
    print("Bienvenidos al juego del ahorcado")
    print("**********************************")
    print("Tu objetivo es adivinar la palabra generada aleatoriamente!")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_acertadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print (f"Te quedan {vidas} vidas y has usado las siguientes letras: {' '.join(letras_acertadas)}")
        palabra_lista = [letra if letra in letras_acertadas else '-' for letra in palabra]
        print(diccionario_vidas[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Elige una letra: ").upper()

        # si la letra seleccionada esta en el abecedarios y no esta en el conjunto de
        # letras que ya se han ingresado antes, se añade la letra al conjunto de letras ingresadas

        if letra_usuario in abecedario - letras_acertadas:
            letras_acertadas.add(letra_usuario)

            # sila letra esta en la palabra quitar la letra del conjunto de letras por adivinar
            # si no esta en la palabra, quitar vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra {letra_usuario} no esta en la palabra!")

        # si la letra escogida por el usuario ya fue elegida en el conuunto de letras adivinadas
        elif letra_usuario in letras_acertadas:
            print("\n Ya escogiste la letra ingresada. Escoge una letra nueva!!")

        else:
            print("\n Esta letra no existe en el abecedario. Elige otra letra!!!")

    if vidas == 0:
        print(diccionario_vidas[vidas])
        print(f"Estas ahorcado!!!!. Perdiste , te quedaste sin vidas!!! La palabra era {palabra}")
    else:
        print(f"Excelente!!!! Adivinaste la palabra!!! La palabra es {palabra}")

ahorcado()
