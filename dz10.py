import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def dz10z01():
    promptKey = "Unesite sifru predmeta: "
    lineKey = input(promptKey)
    course_and_grade_dict = {}
    while lineKey:
        promtValue = "Unesite ocenu za predmet " + lineKey + " :"
        lineValue = input(promtValue)
        course_and_grade_dict[lineKey] = int(lineValue)
        lineKey = input(promptKey)

    print(course_and_grade_dict)
    data = {'Predmeti': course_and_grade_dict.keys(), 'Ocene': course_and_grade_dict.values()}
    df = pd.DataFrame(data=data)
    print(df['Ocene'].value_counts())
    predmetCount = {}
    for predmet in df['Predmeti']:
        predmet = predmet[0:2]
        if predmet in predmetCount:
            predmetCount[predmet] = predmetCount[predmet] + 1
        else:
            predmetCount[predmet] = 1
    print(predmetCount)
    ocena_avg = []
    ocena_avg.append(0)
    print(df['Ocene'])
    for ocena in df['Ocene']:
        print(ocena)
        ocena_avg.append((sum(ocena_avg) + ocena) / (len(ocena_avg)+1))

    print(ocena_avg)
    fig, axs = plt.subplot_mosaic([['upper left', 'upper right'],
                                  ['down', 'down']])

    #Broj ocena
    brojOcena = df['Ocene'].value_counts()
    axs['upper left'].pie(brojOcena.values, labels=brojOcena.keys(), autopct='%1.1f%%',
            shadow=True, startangle=90)
    axs['upper left'].axis('equal')

    #Broj ocena po oznaci predmeta
    y_pos = np.arange(len(predmetCount))
    axs['upper right'].barh(y_pos, predmetCount.values(), align='center')
    axs['upper right'].set_yticks(y_pos, labels=predmetCount.keys())
    axs['upper right'].set_xlabel('Broj ocena')
    axs['upper right'].set_title('Ocene po grupi predmeta')


    axs['down'].plot(ocena_avg, label="Kretanje prosecne ocene sa brojem ocena")
    plt.show()
    plt.savefig('dz10graf.png')

    df.to_csv('courses_and_grades.csv')


if __name__ == '__main__':
    dz10z01()

#
# Domaći zadatak #10 (3h)
# Napisati python program koji beleži informacije o položenim ispitima:
# Student upisuje sa konzole položeni ispit, najpre šifru predmeta, pa ocenu. Ova informacija
# se čuva u imeniku.
# Iz imenika, preko pandas paketa napraviti CSV datoteku u kojoj je jedna kolona Predmet
# (vrednosti su šifre predmeta) a druga kolona Ocena (vrednosti su ocene). Iz ovih podataka, računati:
# • Broj ocena (koliko ima šestica, sedmica, itd).
# • Broj položenih ispita po šifri predmeta (koliko ima CS predmeta, IT predmeta, SE
# predmeta, itd.)
# • Promenu prosečne ocene (kako se menja prosečna ocena po položenom predmetu)
# Na jednoj figuri iscrtati raspored ocena kao pie plot (gornji levi subplot), broj položenih predmeta kao horizontalni bar plot (gornji deni subplot) i promenu prosečne ocene kao linijski plot (donji subplot cele dužine).
# Snimiti Figuru kao Student_izvestaj.png, i CSV datoteku kao Student_izvestaj.csv.