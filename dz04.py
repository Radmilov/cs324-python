#
# Napisati funkciju sa dva ulazna parametra:ime i br_indeks
# Vrednost br_indeks (četvorocifrena promenljiva) određuje broj elemenata u nizu koji se kreira
# unutar funkcije.
# Elementi niza jesu sledeći:
# • Ukoliko je broj slova u promenljivoj ime paran, generisati cele brojeve od 0 do br_indeks
# sa uniformnom raspodelom
# • Ukoliko je broj sloba u promenljivoj ime neparan, generisati razlomljene brojeve u opsegu
# od negativne vrednosti prve dve cifre, to pozitivne vrednosti druge dve cifre u br_indeks.
# Koristiti random biblioteku za generisanje brojeva.
# Sortirati niz korišćenjem for petlje i privremene promenljive.
# Kao povratnu vrednost vratiti sortirani niz.
# U glavnom programu uneti promenljive ime i br_indeks, pozvati funkciju sa tim promenljivima
# i odštampati sortirani niz.
import random


def countOfAlphabetCharacters(string):
        result = 0
        for char in string:
            if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
                result += 1  # same as result = result + 1
        return result

def nameAndIndexOperation(name, index):
    if len(index) != 4:
        return 0
    else:
        arrayOfNumbers = []
        if countOfAlphabetCharacters(name) % 2 == 0:
            for i in range(0, int(index)):
                arrayOfNumbers.append(random.uniform(0, int(index)))
        else:
            for i in range(int(index[0:1])*-1, int(index[2:3])):
                arrayOfNumbers.append(random.uniform(int(index[0:1])*-1, int(index[2:3])))
        for i in range(len(arrayOfNumbers)):
            for j in range(i + 1, len(arrayOfNumbers)):

                if arrayOfNumbers[i] > arrayOfNumbers[j]:
                    arrayOfNumbers[i], arrayOfNumbers[j] = arrayOfNumbers[j], arrayOfNumbers[i]

        return arrayOfNumbers

def fibonaccirecursive(number):
    if number <= 1:
        return number
    else:
        return (fibonaccirecursive(number - 1) + fibonaccirecursive(number - 2))

def fibonacciiterative(number):
    previousnumber = 0
    currentnumber = 1
    for i in range(1, number):
        prepreumber = previousnumber
        previousnumber = currentnumber
        currentnumber = prepreumber + previousnumber
    return currentnumber

   # Rekurzivna metoda je dosta elegantnije napisana ali zauzima dosta vise memorije na stacku i potrebno
   # joj je vise vremena za isvrsavanje. Za jednocifrene parametre performanse su gotovo iste, ali za
   # neke vece brojeve, dvocifrene ili trocifrene, razlika je uocljiva, i razlika je veca kako je i
   # parametar veci.