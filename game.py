# Importar el modulo random porque se va tener una lista de palabras que vamos a necesitar para poder elegir una en el juego
import random
# Importando modulo de python os
import os

# Creando una funcion principal llamada run, codigo principal

# Buscar en google una pequeña lista hangman ascii art de dibujos
# Imagenes del ahorcado


def run():
    IMAGES= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    # Definir una DB
    # creando una lista
    BD = [  
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP"
    ]
    # Pedirle al usuario que ingrese una palabra, pero antes de eso con el modulo random que se acaba de importar, se va elegir de la base de datos BD una palabra aleatoria que es la que va tratar de adivinar el usuario
    word = random.choice(BD)
    # Se crea una lista llamada spaces que va contener guines bajos por (x) la cantidad de letras que yo tenga en mi palabra
    spaces = ["_"] * len(word)
    # Crear serie de intentos
    # Como son 7 imagenes se pondra 6 porque se cuenta desde 0
    attemps = 6

    # Creando ciclo infinito
    while True:
        # Limpiar la pantalla
        os.system("cls")   # se le pasa el comando clear
        # Mostrar los guiones bajos
        for character in spaces:
            # para que este en cada linea/ con espacio
            print(character, end=" ")
        # Quiero que se imprima la imagen en el indice de intentos que tiene el usuario
        print(IMAGES[attemps])
        # Preguntarle al usuario por su eleccion
        # upper todo tiene que estar en mayuscula
        letter = input("Elige una letra: ").upper()

        # Creando una variable
        # Va tener el valor de falso que va indicar si la persona encontro realmente la letra en cada uno de los ciclos
        found = False
        # Hacer los ciclos para ir viendo si los usuarios ingresan las letras
        for idx, character in enumerate(word):
            # Voy a preguntar si caracter es igual a la letra
            if character == letter:
                # Entonces el espacio, en el indice que estoy recorriendo en estos momentos, le pondremos justamente esa letra que adivino el usuario
                spaces[idx] = letter
                # found es igual a true porque la persona justamente encontro una letra
                found = True
        # Si found es false
        if not found:
            # Le voy a restar uno a la variable, porque la persona tiene un intento menos
            attemps -= 1
        # Voy a preguntar, si ya no hay guiones bajos, si el caracter (_) ya no esta en spaces, quiere decir que elusuario gano.
        if "_" not in spaces:
            # Limpiar la pantalla
            os.system("cls")
            # Imprimir al usuario
            print("Ganaste")
            break  # salirme del ciclo
            # Input para cortar el juego  antes de que se salga para que se pueda ver justamente lo que paso
            input()

        # En este if se va preguntar si attemps, es decir si ya no quedan intentos
        if attemps == 0:
            # Limpiar la pantalla
            os.system("cls")
            # Imprimir al usuario
            print("Perdiste")
            break  # salirme del ciclo
            # Input para cortar el juego  antes de que se salga para que se pueda ver justamente lo que paso
            input()


# Creando un enter point
if __name__ == '__main__':
    run()  # se va ejecutar la funcion
