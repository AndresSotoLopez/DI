
def __suma__(num1, num2):
    return (int(num1+num2))

def __resta__(num1, num2):
        return (int(num1-num2))

def __multiplicacion__(num1, num2):
        return (int(num1*num2))

def __division__(num1, num2):
        if(num2 == 0):
            print("\n [!] No se puede realizar la divisiom: !!El divisor es 0!!")
            return
        else:
            return (int(num1/num2))
    
