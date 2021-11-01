# Domaći zadatak #5
# Zadatak #1
# Napraviti klasu dokument sa osobinama ime i broj reči. Izvesti klasu knjiga koja ima dodatne
# osobine autor, žanr, godina izdavanja.
# Instancirati 10 knjiga. Napraviti imenik koji će kao ključ imati broj knjige (počevši od lib001) a
# kao vrednost knjigu. Štampati sve knjige u formatu:
# < broj knjige: žanr, autor, naziv.>


class Document:
    def __init__(self, name, wordcount):
        self.name = name
        self.wordcount = wordcount

class Book(Document):
    def __init__(self, name, wordcount, author, genre, year):
        super().__init__(name, wordcount)
        self.author = author
        self.genre = genre
        self.year = year

    def __str__(self):
        return self.genre + ", " +self.author + ", " + self.name
def z05():
    dict = {
        "lib001": Book("How to escape from hangover 1", 3244, "Radmilo Vukadinovic", "Misterija", 2021),
        "lib002": Book("History 2", 4244, "John Doe", "Thriller", 2022),
        "lib003": Book("Automate the boring stuff with python", 324, "Al Sweigard", "Educational", 2015),
        "lib004": Book("Fight club", 4244, "John Doe", "Thriller", 2022),
        "lib005": Book("Green Mile", 4244, "John Doe", "Drama", 2022),
        "lib006": Book("hitchhiker's guide to the galaxy", 4244, "John Doe", "Sci-Fi", 2022),
        "lib007": Book("Nineteen eighty-four", 4244, "John Doe", "Social", 2022),
        "lib008": Book("To kill a mockingbird", 4244, "John Doe", "Thriller", 2022),
        "lib009": Book("The great gatsby", 4244, "John Doe", "Thriller", 2022),
        "lib010": Book("Dune", 4244, "John Doe", "Sci-Fi", 2022)
    }
    for book in dict:
        print(book + ": " +str(dict[book]))

# Zadatak #2
# Napraviti klasu osoba, koja će imati osobine ime i prezime.
# Nakon toga, izvesti klasu student koja će imati dodatne osobine broj_indeksa, smer, i
# položene ispite.
# Položene ispite napraviti kao imenik gde je ključ šifra predmeta, a ocena vrednost. Napraviti
# dva objekta klase student i popuniti sve osobine.
# Naći da li su studenti na istom smeru ili ne, koliko je koji student položio ispite, i da li imaju
# ispite koje su oba studenta položili

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Person):

    def __init__(self, name, surname, index, studies):
        super().__init__(name, surname)
        self.index = index
        self.studies = studies
        self.courses = {}

def compareStudies(studentone: Student, studenttwo: Student):
    if studentone.studies == studenttwo.studies:
        return True
    else:
        return False

def countOfPassedExams(student: Student):
    count = 0
    for course in student.courses:
        if student.courses[course] > 5:
            count += 1
    return count

def coursesCompletedByBothStudents(studentone: Student, studenttwo: Student):
    for course in studentone.courses:
        if course in studenttwo.courses and studentone.courses[course] > 5 and studenttwo.courses[course] > 5:
            print(course +" has been completed by both " +studentone.name +" and " +studenttwo.name +".")
def z02():
    radmilo3822 = Student("Radmilo", "Vukadinovic", "3822", "SI")
    simeon3821 = Student("Simeon", "Ilic", "3821", "SI")
    sergej3820 = Student("Sergej", "Kubat", "3820", "SI")
    radmilo3822.courses["CS101"] =  6
    radmilo3822.courses["MA202"] = 5
    radmilo3822.courses["CS103"] = 6
    print(countOfPassedExams(radmilo3822))
    simeon3821.courses["CS101"] = 10
    simeon3821.courses["IT101"] = 10
    simeon3821.courses["MA202"] = 10
    print(countOfPassedExams(simeon3821))
    sergej3820.courses["MA202"] = 10
    sergej3820.courses["CS230"] = 10
    sergej3820.courses["CS355"] = 10
    print(countOfPassedExams(sergej3820))
    coursesCompletedByBothStudents(radmilo3822, simeon3821)
    coursesCompletedByBothStudents(radmilo3822, sergej3820)
    coursesCompletedByBothStudents(sergej3820, simeon3821)


