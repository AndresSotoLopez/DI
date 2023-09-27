#Imoports
import os
import random
import time

#Variables Globales
opciones = ["piedra", "papel", "tijeras"]

#Funcion que define tu jugada
def __tuJugada__():

    
    os.system("clear")
    print("-----------------------------------")
    print("\n[+] Elige:")
    print("\n\t[+] Piedra")
    print("\n\t[+] Papel")
    print("\n\t[+] Tijeras")
    print("\n-----------------------------------\n\n")


    while True:
        eleccion = input("\t[+] Eleccion: ")
        if(eleccion.lower() == opciones[0] or eleccion.lower() == opciones[1] or eleccion.lower() == opciones[2]):
            break

    return eleccion

#Funcion que elige una jugada aleatoria
def __jugadaAleatoria__():

    return opciones[random.randint(0,2)]

#Funcion que calcula quien gana
def __quienGana__(opcion2):
    
    opcion1 = __tuJugada__().lower()

    if(opcion1 == opcion2):
        return 0
    
    elif((opcion1 == "piedra" and opcion2 == "tijeras") or (opcion1 == "tijeras" and opcion2 == "papel") or (opcion1 == "papel" and opcion2 == "piedra")):
        return 1

    else:
        return -1
    
#Funcion que nos dice quien ha ganado
def __jugadas__():
    
    victorias = 0
    opcion2 = __jugadaAleatoria__()

    win = __quienGana__(opcion2)

    if(win == 1):
        victorias = victorias + 1
        print("\n\t[+] Has Ganado!!!\t [!] El oponente perdió con: " + opcion2)
    elif(win == -1):
        print("\n\t[+] Has perdido!!!\t [!] El oponente ganó con: " + opcion2)
    else:
        print("\n\t[+] Has empatado!!!")
    
    return win


def __main__():

    juegos = 0
    victorias = 0
    while juegos < 5:
        victorias += __jugadas__()
        juegos += 1
        if(juegos != 5):
            time.sleep(3)

        if(victorias < 0):
            victorias = 0

    print("\n[+] Has ganado " + str(victorias) + " veces, enhorabuena!!" )

__main__()