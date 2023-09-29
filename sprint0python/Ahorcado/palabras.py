##Fichero con las palabras

#Imports
import random

def __faciles__():

    faciles = ["casa", "agua", "azul"]
    return faciles[random.randint(0,len(faciles)-1)]

def __Normales__():

    normales = ["garaje", "cabeza", "guardia"]
    return normales[random.randint(0,len(normales)-1)]

def __Dificiles__():

    dificiles = ["curiosidad", "paracaidas", "coagulacion"]
    return dificiles[random.randint(0,len(dificiles)-1)]