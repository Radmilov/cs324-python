import matplotlib.pyplot as plt

def dz09z01():
    a = {}
    b = []
    prompt = "Unesite ocenu: "
    line = input(prompt)

    while line:
        if int(line) > 10 or int(line) < 6:
            print("Ispit mora biti polozen kako bi bio unet u program.\nDozvoljen unos od 6 do 10")
            line = input(prompt)
        else:
            if int(line) not in a:
                a[int(line)] = 1
            else:
                a[int(line)] = a[int(line)] + 1
            if len(b) > 1:
                b.append(int((sum(b) + int(line)) / (len(b)+1)))
            else:
                b.append(int(line))
            line = input(prompt)

    print(a)
    print(b)
    # Prosecna ocena
    plt.plot(b, label="Prosecna ocena")
    plt.xlabel('Broj polozenih ispita')
    plt.ylabel('Ocena')
    plt.xlim(0, len(b))
    plt.ylim(5.5, 10.5)
    plt.grid()
    plt.title('Prosecna ocena')
    plt.savefig('prosecna_ocena.png')
    plt.legend(loc='best')
    plt.close()

    #Pojedinacna ocena
    fig1, ax1 = plt.subplots()
    ax1.pie(a.values(), labels=a.keys(), autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Pojedinacna ocena')
    plt.savefig('pojedinacna_slika.png')
    plt.close()
    

if __name__ == '__main__':
    dz09z01()



#Napisati program koji će za svaki položeni ispit računati prosečnu ocenu:
#Sa tastature se unosi ocena (ne sme biti manja od 6) sve dok se ne pritisne ENTER. Prilikom svakog unosa računa se prosečna ocena za (do tada) unete ocene.
#Prvi grafikon štampa prosečna ocenu: iscrtava promenu prolazne ocene sa brojem položenih ispita.
#Drugi grafikon štampa broj pojedinačnih ocena u pie grafikonu.