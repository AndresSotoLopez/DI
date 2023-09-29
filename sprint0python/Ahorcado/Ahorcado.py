#Imports 
import os 
import random
import time
from palabras import __faciles__, __Normales__, __Dificiles__
from muñeco import __muñeco__

#Variables globales
errores = 0

#Funcion para limpiar la pantalla
def __borrarConsola__():
    os.system("clear")

#Funcion que nos muestra el menu de opciones existentes para elegir la dificultad de las palabras
def __menu__():

    __borrarConsola__()
    print("\n----------------------Menu----------------------")
    print("\n\t[A] Faciles.")
    print("\n\t[B] Normales.")
    print("\n\t[C] Dificiles.")
    print("\n------------------------------------------------\n")

    #Bucle para comprobar que las opciones introducidas sean las especificadas en el menu
    while True:
        opcion = input("\t[+] Opcion: ").lower()
        if(opcion == "a" or opcion == "b" or opcion == "c"):
            break

    return opcion

#Funcion que nos retorna una palabra de forma aleatoria una palabra (Comprobar archivo palabras.py)
def __palabraAleatoria__():

    opcion = __menu__()

    if(opcion == "a"):
        return __faciles__()
    elif (opcion == "b"):
        return __Normales__()
    else:
        return __Dificiles__()    
    
#Funcion que muestra la palabra oculta actualizada en cada jugada, las letras introdicidas erroneas y el numero de errores
def __PEL__(PO, letras, error):
    print("\n[+] Palabra: " + str(PO) + "\t[+] Letras: " + str(letras) + "\t[+] Nº de errores:" + str(error)) 

#Funcion que nos permite ir letra a letra comparando si la letra que hemos introducido es igual a la letra[i] de la palabra
def __comprobarLetra__(letra, palabra):

    for i in range(len(palabra)):
        if(letra == palabra[i]):
            return True

    return False

#Funcion que nos retorna la palabra actualizada
def __nuevaPO__(letra, palabra, PO):

    palabraOculta = ""

    #Bucle para formar la nueva palabraOculta
    for i in range(len(PO)):

        #En el caso de que en la palabraOculta anterior el valor en i no equivalga a "_", se añadirá la letra que tenga ese espacio
        if(PO[i] != "_"):
            palabraOculta += PO[i]

        #Si la letra que mandamos es igual que la letra de la palabra no oculta segun i, añadimos esa letra a la nueva palabra oculta
        elif(letra == palabra[i]):
            palabraOculta += str(letra)

        #En cualquier otro caso, se añadiran "_"
        else:
            palabraOculta +=  "_"

    return palabraOculta    


def __interface___():
    
    #Variables
    palabra = __palabraAleatoria__().lower()
    palabraOculta = ""
    error = 0
    letras = ""
    
    #Formaremos la palabra oculta a partir de la longitud de la palabra aleatoria que se ha generado
    for i in range(len(palabra)):
        palabraOculta += "_"
    
    #Bucle para contar los errores
    while True:


        __borrarConsola__()
        print(__muñeco__(error))
        __PEL__(palabraOculta, letras, error)

        #Condicional para que en el caso de que se adivine la palabra, se salga del bucle y nos permita elegir si queremos volver a jugar o no
        if(palabraOculta == palabra):
            break
        
        #Condicional que nos permite salir del bucle en el caso de que superemos los errores permitidos
        if(not error < 6):
            break

        letra = input("\n\t[+] Letra: ").lower()
        
        #Condicionales que nos permiten comprobar si la letra existe en la palabra en caso afirmativo, se redirige el codigo a la funcion __nuevaPO_()
        if(__comprobarLetra__(letra, palabra)):
            palabraOculta = __nuevaPO__(letra, palabra, palabraOculta)
        
        #En caso contrario, si es el primer error, solo se añadira la letra, en caso contrario se añadira ", " antes de añadir la letra
        else:
            if (error != 0):
                letras += ("," + letra)
            else:
                letras += letra

            error += 1
           
    #Condicional que nos permite saber si hemos ganado o perdido    
    if(palabraOculta != palabra):
        print("\n\t[!] Has perdido!!!\t[!] La palabra era: " + palabra)
    else:
        print("\n\t[!] Has Ganado!!!")

def __main__():
        
    #Bucle que nos permite seguir jugando en caso de indicarlo con la opcion S
    while True:

        __interface___()

        #Comprobamos que las opciones que introducimos son correctas en este caso S o N
        while True:
            bucle = input("\n\t[?] Jugar otra vez S/N: ").lower()
            if (bucle == "s" or bucle == "n"):
                break
    
        if(bucle == "n"):
            break
__main__()
