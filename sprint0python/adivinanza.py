#Imports
import os

#Variables globales
NumeroAdivinanzas = 3;


#Nuevo metodo donde se iteren las adivinanzas.
def __adivinanzas__(iterador):

    adivinanza = ["Aunque tengo cuatro patas, yo nunca puedo correr, tengo la comida encima, y no la puedo comer.", "¿Qué es lo que sopla sin boca y vuela sin alas?", "¿Qué es lo que desaparece cuando se lo nombra?"]

    print(adivinanza[iterador])


#Funcion para mostrar las soluciones segun el iterador que le llegue a la funcion.
def __soluciones__(iterador):
    
    soluciones = ["Mesa-Silla-Sofa", "El viento-El sonido-El Calor", "El silencio-El frio-El agua"]
    print("\t[A] " + soluciones[iterador].split("-", 3)[0] + "\n\t[B] " + soluciones[iterador].split("-", 3)[1] + "\n\t[C] " + soluciones[iterador].split("-", 3)[2] + "\n\n--------------------------------------------\n")


def __puntuacion__():

    opcion = "h"
    while opcion.lower() != "a" and opcion != "b" and opcion != "c":
        opcion = str(input("[+] Opción: ").lower())
    
    if opcion.lower() == "a":
         print("[!!] Enhorabuena has acertado!!!!\n")
         return 10;
    else:
        print("[!!] No has acertado la adivinanza!!!\n")
        return 5;


# Definición de función main del programa.
def __main__():

    os.system("clear")
    puntos = 0
    puntuacion = 0

    for i in range(NumeroAdivinanzas):
        print("\n[+] Adivina adivinanza: ")
        print("--------------------------------------------\n")
        __adivinanzas__(i)
        print("\n--------------------------------------------\n[+] Opciones:\n")  
        __soluciones__(i)
        puntuacion = __puntuacion__()
        os.system("clear")

        if puntuacion == 10:
            puntos += 10
        else:
            puntos -= 5

        

    print("\n---------------------------------------\n\n\t[+] Puntos conseguidos: " + str(puntos) + "\n\n---------------------------------------")

__main__()
