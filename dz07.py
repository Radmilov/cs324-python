import re

def z01():
    with open("../resources/dz07.txt", "r") as txt:
        lines = txt.readlines()
        index = "3822"
        pattern = re.compile(index[0])
        count = 0
        for line in lines:
            if (count - 2) % 5 == 0 and pattern.match(line[0]):
                print(line)
            count += 1

def z02():
    import sqlite3
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("""CREATE TABLE predmeti(
        code text,
        name text,
        professor integer,
        year integer
        )""")

    def search_by_professor(professorName):
        with conn:
            result = c.execute("SELECT * from predmeti WHERE professor = :professorName", {'professorName': professorName})
            result = result.fetchall()
            if result is not None:
                print(result)
            else:
                print("No courses found for this professor.")

    class predmeti:
        def __init__(self, code, name, professor, year):
            self.code = code
            self.name = name
            self.professor = professor
            self.year = year

        def save(self):
            with conn:
                c.execute("INSERT INTO predmeti VALUES (:code, :name, :professor, :year)",
                {
                    'code': self.code, 'name': self.name, 'professor': self.professor, 'year': self.year 
                })


    cs101 = predmeti('CS101', 'Uvod u OOP', 'Vladimir Milicevic', 2019)
    cs230 = predmeti('CS230', 'Web sistemi 1', 'Vladimir Milicevic', 2021)
    ma101 = predmeti('MA101', 'Matematika 1', 'Rale Nikolic', 2019)
    cs324 = predmeti('CS324', 'Skripting jezici', 'Nemanja Zdravkovic', 2021)
    cs101.save()
    cs230.save()
    ma101.save()
    cs324.save()
    search_by_professor('Vladimir Milicevic')
    search_by_professor('Nemanja Zdravkovic')
    search_by_professor('Null')