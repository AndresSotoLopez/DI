
#Funcion de suma
def __suma__(num1, num2):
    return (int(num1+num2))

#Funcion de resta
def __resta__(num1, num2):
        return (int(num1-num2))

#Funcion de multiplicacion
def __multiplicacion__(num1, num2):
        return (int(num1*num2))

#Funcion de division
def __division__(num1, num2):
        #Control de division por 0
        if(num2 == 0):
            print("\n[!] No se puede realizar la division: !!El divisor es 0!!")
            return
        else:
            return (int(num1/num2))
    
