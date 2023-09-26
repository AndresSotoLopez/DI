#Imports
from operaciones import __suma__, __resta__, __multiplicacion__, __division__
import os

#Funcion para limpiar la consola
def __ClearConsole__():
    os.system("clear")

#Lista de opciones
def __opciones__():

    print("\n[+]Opciones:\n\n-----------------------------------\n")
    print("\t[S] Suma")
    print("\n\t[R] Resta")
    print("\n\t[M] Multiplicacion")
    print("\n\t[D] Division")
    print("\n-----------------------------------\n")

#Funcion que nos permite elegir la opcion
def __menu__():

    __opciones__()

    opcion = "h"

    #Bucle para que la funcion no retorne una opcion que no sea valida
    while opcion != "s" and opcion != "r" and opcion != "m" and opcion != "d":
        opcion = input("\n\t[+] Opcion: ").lower()

    return opcion

#Fucnion para pedir el primer numero
def __numero1__():

    num1 = "f"
    
    #Mientas el num1 no sea digito nos va a preguntar de nuevo por el numero.
    while (not num1.isdigit()):
        num1 = input("\n\t\t[+] Introduce el numero 1: ")

    return int(num1)

#Fucnion para pedir el segundo numero
def __numero2__():

    num2 = "f"
    #Mientas el num2 no sea digito nos va a preguntar de nuevo por el numero.
    while (not num2.isdigit()):
        num2 = input("\n\t\t[+] Introduce el numero 2: ")

    return int(num2)

#Funcion para realizar las operaciones
def __operaciones__(opcion):

    #Opcion de suma
    if opcion == "s":
            print("\n\t[+] El resultado de la suma es: " + str(__suma__(__numero1__(),__numero2__())))
    
    #opcion de resta
    elif opcion == "r":
        print("\n\t[+] El resultado de la resta es: " + str(__resta__(__numero1__(),__numero2__())))

    #Opcion de multiplicacion
    elif opcion == "m":
        print("\n\t[+] El resultado de la multiplicacion es: " + str(__multiplicacion__(__numero1__(),__numero2__())))

    #Opcion de division
    else:
        num1 = __numero1__()
        num2 = __numero2__()
        if num2 != 0:
            print("\n\t[+] El resultado de la division es: " + str(__division__(num1,num2)))
        else:
            __division__(num1, num2)
    

def __main__():

    #Bucle para repetir siempre que se ponga si
    while True:
        __ClearConsole__()
        bucle = "j"

        __operaciones__(__menu__())   

        #Bucle para saber si se quiere hacer otra operacion
        while bucle != "s" and bucle != "n":
            bucle = str(input("\n[?] Otra operacion (S/N): ").lower())

        if bucle != "s":
            __ClearConsole__()
            break

__main__()