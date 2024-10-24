import random

palabras = [ 
    "python",
    "programacion",
    "ahorcado",
    "computadora",
    "algoritmo",
    "desarrollo",
    "tecnologia",
    "juego",
    "diversion",
]

intentos = 6

palabra_en_juego = list(palabras[random.randint(0, len(palabras) - 1)])

letras_en_juego = set(palabra_en_juego)

letras_usadas = []

tamaño = len(palabra_en_juego)

palabra_encontrada = [" " for i in range(tamaño)]

while True:
    print(palabra_encontrada)
    print("Intentos Restantes: ", intentos)
    letra_actual = input("Ingresa tu Letra a Buscar: ")
    
    if letra_actual in letras_en_juego and letra_actual not in letras_usadas:
        letras_usadas.append(letra_actual)
        for i in range(0, tamaño):
            if palabra_en_juego[i] == letra_actual:
                palabra_encontrada[i] = letra_actual

        letras_en_juego.remove(letra_actual)

    else:
        letras_usadas.append(letra_actual)
        intentos -= 1

    if len(letras_en_juego) == 0:
        print(palabra_encontrada)
        print("G A N A D O R")
        break
    elif intentos == 0:
        print("A H O R C A D O")
        print("Palabra: ", palabra_en_juego)
        break
