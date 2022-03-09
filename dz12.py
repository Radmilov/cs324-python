import csv
from random import randrange, randint
import numpy as np
import pandas as pd
import sklearn as sklearn
from matplotlib import pyplot as plt
from sklearn import linear_model


def dz12():
    # Ukoliko je vrednost kolone #1 između 8 i 10,
    # povećati vrednost kolone #6 za jedan. Ukoliko
    # je vrednost kolone #4 između 5 i 12, smanjiti
    # vrednost kolone #6 za jedan, a između 13 i 15,
    # smanjiti vrednost kolone #6 za 2. Ukoliko je vrednost
    # kolone #3 između 9 i 10, povećati vrednost kolone #6 za 1.
    # Svuda gde je vrednost kolone #5 nula, vrednost kolone #6 je 5.
    # Obratiti pažnju da pri promeni vrednosti kolona da minimalne i maksimalne vrednosti ostanu nepromenjene.
with open('./dataset.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header

    # write the data
    headers = ['cs_101_ocena', 'it_101_ocena', 'ma_101_ocena', 'cs_115_izostanci', 'cs_115_polozen', 'cs_115_ocena']
    writer.writerow(headers)
    row = {}
    for i in range(0, 10):
        row[headers[0]] = randrange(5,11)
        row[headers[1]] = randrange(5,11)
        row[headers[2]] = randrange(5,11)
        row[headers[3]] = randrange(16)
        row[headers[4]] = randint(0, 1)
        row[headers[5]] = randrange(5, 11)
        if row[headers[0]] == 9 and row[headers[5]] < 10:
            row[headers[5]] = row[headers[5]] + 1
        if row[headers[3]] > 5 and row[headers[3]] < 12 and row[headers[5]] > 5:
            row[headers[5]] = row[headers[5]] - 1
        elif row[headers[3]] == 14 and row[headers[5]] > 6:
            row[headers[5]] = row[headers[5]] - 2
        if row[headers[2]] > 9 and row[headers[5]] < 10:
            row[headers[5]] = row[headers[5]] + 1
        if row[headers[4]] == 0:
            row[headers[5]] = 5
        writer.writerow(row.values())

    # 1. Istrenirati model linearna regresije da estimira vrednosti
    # kolone cs_115_ocena, ako su ulazni podaci: • Samo kolona cs_101 ocena,
    # • Samo kolona cs_115_izostanci, • Sve kolone (osim cs_115_ocena i cs_115_polozen,
    # naravno) Istrenirati modele linearne regresije (koristiti 75%, a zatim 90% skupa
    # za trening skup) za svaku od traženih kolona, naći broj grešaka i tačnost za svaki
    # , i zaključiti koji je model najbolje koristiti. Kada se koristi samo jedna kolona
    # , nacrtati i grafike estimiranih vrednosti naspram pravih vrednosti.

samo_cs101_ocena = headers[0]
samo_cs115_izostanci = headers[3]
sve_kolone = headers
target = headers[5]
df = pd.read_csv('dataset.csv')
data_needed = [samo_cs115_izostanci, target]
data = df[data_needed]
samo_cs115_izostanci_data = np.array(data.drop(target, 1))
samo_cs115_izostanci_predict = np.array(data[target])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(samo_cs115_izostanci_data, samo_cs115_izostanci_predict,
test_size=0.1)
print(len(x_train), len(x_test))

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

predictions = linear.predict(x_test)
new_df = pd.DataFrame(x_test, columns=[samo_cs115_izostanci])
new_df['Y'] = y_test
new_df['Predikcija 90%'] = predictions

accuracy = linear.score(x_test, y_test)
print("Preciznost sa odnosom 90:10 - " +str(accuracy))
fig, axs = plt.subplots(3, 1)
axs[0].scatter(new_df[samo_cs115_izostanci], y_test,  color='blue')
axs[0].plot(new_df[samo_cs115_izostanci], predictions, color='red')
print(len(x_train), len(x_test))
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(samo_cs115_izostanci_data, samo_cs115_izostanci_predict,
test_size=0.3)
print(len(x_train), len(x_test))

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

predictions = linear.predict(x_test)
new_df = pd.DataFrame(x_test, columns=[samo_cs115_izostanci])
new_df['Y'] = y_test
new_df['Predikcija 90%'] = predictions

accuracy = linear.score(x_test, y_test)
print("Preciznost sa odnosom 70:30 - " +str(accuracy))
axs[1].scatter(new_df[samo_cs115_izostanci], y_test,  color='blue')
axs[1].plot(new_df[samo_cs115_izostanci], predictions, color='red')
plt.show()









if __name__ == '__main__':
    dz12()


# Napisati program koji će generisati skup podataka koji će se koristiti za trening i test skupove. Podaci jesu sledeći:
# • Kolona #1: Ime: cs_101_ocena (vrednost od 5 do 10)
# • Kolona #2: Ime: it_101_ocena (vrednost od 5 do 10)
# • Kolona #3: Ime: ma_101_ocena (vrednost od 5 do 10)
# • Kolona #4: Ime: cs_115_izostanci (vrednosti od 0 do 15)
# • Kolona #5: Ime cs_115_položen (vrednosti 0 ili 1)
# • Kolona #6: Ime: cs_115_ocena (vrednosti od 5 do 10)
# Kolone popuniti nasumično, i onda promeniti sledeće (ne ručno, već kroz kod):
