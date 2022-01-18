import dz06
from dz01 import isStepenBroja2
from dz02 import allPrimeNumbersBetweenParameters
from dz03 import inputClassesAndGrades, generateRandomBetweenParametersAndSort, generateUniformNumbers
from dz04 import nameAndIndexOperation, fibonaccirecursive, fibonacciiterative
from dz05 import z05, z02
from dz06 import z01, z02
import dz08

def main():
    print(fibonaccirecursive(12))
    print(fibonacciiterative(12))
    z05()
#    z02()
    z01()
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [1, 2, {}, 4, 5]
    print(dz06.z02(lista1))
    #dz06.z02(lista2)
    dz08.z01()
    dz08.z02()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

    
    #DZ01
    #brojevi = [1,2,256,512,777, 553, 128, 658, 523525]
    #for broj in brojevi:
    #    print('Broj ' +str(broj) +' je stepen broja 2: '+str(isStepenBroja2(broj)))

    #DZ02
    #primeNumbers = allPrimeNumbersBetweenParameters(1, 100)
    #print(primeNumbers)

    #DZ03

    #Zadatak 1
    #inputClassesAndGrades()
    #Zadatak 2
    #generateRandomBetweenParametersAndSort(5)

    #Zadatak 3


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
