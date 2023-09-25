# Variables globales
adivinanza = "Aunque tengo cuatro patas, yo nunca puedo correr, tengo la comida encima, y no la puedo comer."


# Definición de función main del programa.
def __main__():
    print("\n[+] Adivina adivinanza: ")
    print("--------------------------------------------\n")
    print(adivinanza)
    print("\n--------------------------------------------\n[+] Opciones:\n")
    print(
        "\t[A] Mesa\n\t[B] Sofa\n\t[C] Silla\n\n--------------------------------------------\n"
    )

    # Inicializar la variable antes de entrar al bucle while.
    opcion = "h"

    # Bucle while para comprobar que las opciones solo sean las 3 que se muestran.
    while opcion.lower() != "a" and opcion.lower() != "b" and opcion.lower() != "c":
        opcion = input("[+] Opción: ")

    # Comprobar la respuesta del usuario.
    if opcion.lower() == "a":
        print("[!!] Enhorabuena has acertado!!!!\n")
    else:
        print("[!!] No has acertado la adivinanza!!!\n")


__main__()
