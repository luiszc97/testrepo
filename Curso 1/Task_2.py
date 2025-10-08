def getFactors(numero):
    """
    función que devuelve una lista de factores de un número dado x. Básicamente, 
    encuentra los números entre 1 y el entero dado que dividen el número de forma 
    uniforme.
    """
    listFac = []
    if (numero == 1):
        listFac = [1]
        return listFac

    for num in range(1,numero+1):
        if (numero % num == 0):
            listFac.append(num)
    
    return listFac

def isPrime(numero):
    """
    función que devuelve si el número dado x es primo o no. Esta función devuelve 
    un booleano.
    """
    listPrime = getFactors(numero)
    if (len(listPrime) == 2):
        return True
    else:
        return False


def isComposite(numero):
    """
    función que devuelve si el número dado x es o no compuesto. Esta función devuelve 
    un booleano. Pretendemos que reutilice aquí código de la función de número primo.
    """
    if numero == 1:
        return False
    elif isPrime(numero) == False:
        return True
    else:
        return False
    
def isPerfect(numero):
    """
    función que devuelve si el número dado x es perfecto o no. Esta función 
    devuelve un booleano.
    """
    listPerfecto = getFactors(numero)
    listPerfecto.pop()
    numSum = 0
    for num in listPerfecto:
        numSum += num

    if numSum == numero:
        return True
    else:
        return False
    
def isAbundant(numero):
    """
    función que devuelve si el número dado x es abundante o no. Esta función devuelve un booleano.
    """
    listAbundat = getFactors(numero)
    listAbundat.pop()
    numSum = 0
    for num in listAbundat:
        numSum += num

    if numSum > numero:
        return True
    else:
        return False

def isTriangular(numero):
    """
    función que devuelve si el número dado x es triangular o no. Esta función devuelve un booleano.
    """
    n = 1
    while (n * (n+1))/2 <= numero:
        if (n * (n + 1)) // 2 == numero:
            return True
        n += 1

    return False

    
def isNarcissistic(numero):
    """
    función que devuelve si un número dado x es o no narcisista. Esta función devuelve un booleano.
    """
    numSum = 0
    numCifras = len(str(numero))
    for cifra in str(numero):
        numSum += int(cifra) ** numCifras
    
    if numSum == numero:
        return True
    else:
        return False


def main():

    playing = True
    while playing == True:

        num_input = input('Give me a number from 1 to 10000.  Type -1 to exit. ')

        try:
            num = int(num_input)

            if (num == -1):
                playing = False
                continue

            if (num <= 0 or num > 10000):
                continue

            factors = getFactors(num)
            print("The factors of", num, "are", factors)

            if isPrime(num):
                print(str(num) + ' is prime')
            if isComposite(num):
                print(str(num) + ' is composite')
            if isPerfect(num):
                print(str(num) + ' is perfect')
            if isAbundant(num):
                print(str(num) + ' is abundant')
            if isTriangular(num):
                print(str(num) + ' is triangular')
            if isNarcissistic(num):
                print(str(num) + ' is narcissistic')

        except ValueError:
            print('Sorry, the input is not an int.  Please try again.')
            
#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()