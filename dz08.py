import numpy as np

def z01():
    array_one = np.zeros((3,3), dtype='int32')
    arr = [1, 1, 1]
    np.fill_diagonal(array_one, arr)
    print(array_one)

    array_two = np.zeros((4,4), dtype='int32')
    tens = np.full((2,2), 10)
    array_two[1:-1, 1:-1] = tens
    print(array_two)

    array_three = np.ones((5,5), dtype='int32')
    zeroes = np.zeros((3,3), dtype='int32')
    zeroes[1,1] = 1
    array_three[1:-1, 1:-1] = zeroes
    print(array_three)


import sqlite3
import pandas as pd

def z02():
    conn = sqlite3.connect('biblioteka.db')
    c = conn.cursor()
    c.execute("""DROP TABLE IF EXISTS knjige;""")
    c.execute(""" CREATE TABLE knjige(
            katBroj text,
            naslov text,
            izdavac text,
            godinaIzdavanja integer,
            izdat text DEFAULT 'False'
            )""")

    def pronadji_sve_knjige():
        with conn:
            result = c.execute("SELECT * from knjige")
            result = result.fetchall()
            if result is not None:
                print(result)
            else:
                print("No books found.")

    def podesi_izdat(katBroj):
        with conn:
            c.execute("UPDATE knjige SET izdat = \'True\' WHERE katBroj = :br ;", { 'br': katBroj})
            if c.rowcount > 0:
                print("Successfull update for " +katBroj)
            else:
                print("No books found by that katBroj.")

    def pronadji_knjige_nakon_godine(godina):
        with conn:
            result = c.execute("SELECT * from knjige WHERE godinaIzdavanja > :godina", { 'godina': godina})
            result = result.fetchall()
            if len(result) > 0:
                print(result)
                return result
            else:
                raise Exception('No books found after input year.')

    class knjiga:
        def __init__(self, katBroj, naslov, izdavac, godinaIzdavanja):
            self.katBroj = katBroj
            self.naslov = naslov
            self.izdavac = izdavac
            self.godinaIzdavanja = godinaIzdavanja
            self.izdat = 'False'

        def save(self):
            with conn:
                c.execute("INSERT INTO knjige VALUES (:katBroj, :naslov, :izdavac, :godinaIzdavanja, :izdat)",
                {
                    'katBroj': self.katBroj, 'naslov': self.naslov, 'izdavac': self.izdavac, 'godinaIzdavanja': self.godinaIzdavanja,
                    'izdat': self.izdat
                })


    book = knjiga('1', 'The Nightingale', 'Kristin Hannah', 2019)
    book.save()
    book = knjiga('2', 'The Art Of Programming', 'John Doe', 2015)
    book.save()
    book = knjiga('3', 'Small Boat', 'Noah Ark', 202)
    book.save()
    book = knjiga('4', 'Apocalypse', 'Ronald Windsor', 2224)
    book.save()
    pronadji_sve_knjige()
    podesi_izdat('1')
    podesi_izdat('3')

    pronadji_sve_knjige()
    try:
        pronadji_knjige_nakon_godine(2022)
    except Exception as e:
        print(e)
    savremene_knjige = pd.read_sql_query("SELECT * from knjige WHERE godinaIzdavanja > 2000", conn)
    print(savremene_knjige.head())
    izdate_knjige = pd.read_sql_query("SELECT * from knjige where izdat = 'True'", conn)
    header = ["naslov", "izdavac", "godinaIzdavanja"]
    pd.DataFrame.to_csv(izdate_knjige, "./izdate_knjige.csv", columns=header)

#     //Preko pandas paketa učitati sadržaj tabele knjige. Napraviti novi DataFrame objekat
# savremene_knjige koji će sadržati knjige kod kojih je godina izdavanja od 2000. godine
# Upisati u csv datoteku sve knjige koje su izdate u datoteku izdate_knjige.csv sa kolonama
# Naslov, izdavac, godinaIzdavanja.

