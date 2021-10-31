#DZ01
import random


def inputClassesAndGrades():
    numberOfClasses = int(input("Input your number of classes attended: "))
    classesAndGrades = {}
    for i in range(0, numberOfClasses):
        nameOfClass = input("Input class name: ")
        classesAndGrades[nameOfClass] = int(input("Unesite ocenu na predmetu: "))

    nameOfClass = input("Input class name to see if you passed: ")

    if classesAndGrades[nameOfClass] > 5:
        print("Course "+nameOfClass+" passed with an " +str(classesAndGrades[nameOfClass]))
    else:
        print("Course "+nameOfClass+" not passed.")

    print(classesAndGrades)

#DZ02
from random import randint
def generateRandomBetweenParametersAndSort(num):
    listOfStudentIDs = []
    for i in range(0, num):
        listOfStudentIDs.append(randint(1000, 9999))

    print(listOfStudentIDs)

#DZ03
def generateUniformNumbers():
    index = 3822;
    m = index / 3
    numbers = {}
    for i in range(0,int(m)):
        number = random.uniform(int(str(index)[0:1]), int(str(index)[2:3]))
        numbers[i] = number
    print('Number: ', numbers[index % 3])
    return numbers[index % 3]
