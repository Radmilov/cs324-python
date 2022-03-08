import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def dz11():
    with open('dz11.csv') as csv_file:
        headers = ["StudentID","Univerzitet", "NivoStudija","StudijskiProgram","Trajanje"]
        df = pd.read_csv(csv_file, names=headers)
        print(df['Trajanje'].array)
        avg_studies_length = np.mean(df['Trajanje'].array)
        print(avg_studies_length)
        avg_per_studies = df.groupby('NivoStudija', as_index=False)['Trajanje'].mean()
        print(avg_per_studies)
        mode_per_studies = df.groupby('StudijskiProgram', as_index=False)['Trajanje'].apply(lambda x: x.value_counts().index[0]).reset_index()
        print(mode_per_studies)
        univerziteti = df['Univerzitet']
        broj_univerziteta = len(univerziteti.unique())
        fig, axs = plt.subplots(2 + broj_univerziteta)
        axs[0].axvline(avg_studies_length, color='red', label='Srednja vrednost trajanja studija',
                    linewidth=2)
        axs[0].hist(df['Trajanje'].array, bins=df['Trajanje'].unique().sort(), edgecolor='black')
        print(univerziteti)
        axs[1].hist(univerziteti)
        i = 2
        for univerzitet in univerziteti.unique():
            row = df[df['Univerzitet'].__eq__(univerzitet)]['StudijskiProgram'].value_counts()
            axs[i].pie(row.values, labels=row.keys(), autopct='%1.1f%%',
                                  shadow=True, startangle=90, textprops={'fontsize': 4})
            axs[i].axis('equal')
            i = i + 1
        plt.tight_layout()
        plt.savefig('dz11.png')
        plt.show()




if __name__ == '__main__':
    dz11()


# Napisati program u Python jeziku koji će naći sledeće:
# • Srednju vrednost trajanja studija na svim studijskim programima,
# • Srednju vrednost trajanja studija na pojedinačnim studijskim programima (BAS; MAS;
# DAS)
# • Najčešću vrednost trajanja studija po pojedinačnim studijskim programima,
# • Najčešću vrednost trajanja studija po univerzitetima,
# • Histogram broja studenata po trajanju studija, za naznačenom srednjom vrednošću,
# • Histogram broja studenata po univerzitetu
# • Pie grafikone raspodele studenata po studijskom programu, po univerzitetu,