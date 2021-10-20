def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def numarRegasitDeLaoPozitieData(x, y, lst):
    '''
    Afiseaza "DA" dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție
citită de la tastatură, "NU" in caz contrar.
    :param x: Numar natural, indica pozitia de la care se incepe cautarea numarului.
    :param y: Numar natural, indica nuamrul cautat in lista.
    :param lst: Lista de numere intregi.
    :return: Returneaza (afiseaza in consola) "DA" in caz ca numarul se regasesste in lista incepand de la respectiva pozitie, "NU" in caz contrar.
    '''
    for i in range(x, len(lst), 1):
        if lst[i] == y:
            return print("DA")
    return print("NU")


def sumaTuturorNumerelorIntregi(lst):
    '''
    Calculeaza suma tuturor numerelor întregi pare din lista.
    :param lst: Lista de numere intregi.
    :return: Returneaza suma numerelor intregi pare din lista.
    '''
    sum = 0
    for x in lst:
        if x % 2 == 0:
            sum += x
    return sum


def test_sumaTuturorNumerelorIntregi():
    assert sumaTuturorNumerelorIntregi([1, 3, 2, 1, 2, 2, 5, 6]) == 12
    assert sumaTuturorNumerelorIntregi([]) == 0


def numerePareDinLista(lst):
    '''
    Determina toate numere din lista care sunt pare. Daca se repeta un numar, acesta va apărea în
lista rezultat doar o singura data.
    :param lst: Lista de numere intregi.
    :return: Returneaza lista creata cu numerele pare din lista initiala.
    '''
    rezultat = []
    for x in lst:
        if x % 2 == 0 and not x in rezultat:
            rezultat.append(x)
    return rezultat


def test_numerePareDinLista():
    assert numerePareDinLista([1, 2, 3, 4, 2, 1, 2, 6]) == [2, 4, 6]
    assert numerePareDinLista([]) == []
    assert numerePareDinLista([1, 3, 5]) == []


def procesareLista(lst):
    '''
    Proceseaza lista astfel incat sa se creeze o lista prin înlocuirea fiecărui număr cu un tuplu format din două numere de pe
    poziții distincte din listă care adunate dau acel număr, dacă se poate. Dacă există mai multe soluții o va alege pe prima, iar
    dacă nu se poate, nu se înlocuiește numărul.
    :param lst: Lista de numere intregi.
    :return: Returneaza lista dupa procesare.
    '''
    rezultat = []
    for x in lst:
        ok = 0
        for y in lst:
            for z in lst[y::]:
                if x == y + z:
                    rezultat.append((y, z))
                    ok = 1
                    break
            if ok == 1:
                break
        if ok == 0:
            rezultat.append(x)
    return rezultat


def test_procesareLista():
    assert procesareLista([1, 3, 2, 4]) == [1, (1, 2), 2, (1, 3)]
    assert procesareLista([1, 3, 5, 7]) == [1, 3, 5, 7]


def alltests():
    test_sumaTuturorNumerelorIntregi()
    test_numerePareDinLista()
    test_procesareLista()


def main():
    alltests()
    lst = []
    while True:
        print("1. Citire lista")
        print("2. Afișați dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție "
              "citită de la tastatură.")
        print("3. Afișați suma tuturor numerelor întregi pare din lista.")
        print("4. Afișați toate numere din lista care sunt pare.")
        print("5. Afișați lista obținută prin înlocuirea fiecărui număr cu un tuplu format din două numere de pe "
              "poziții distincte din listă care adunate dau acel număr")
        print("a. Afisare lista")
        print("x. Iesire")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citireLista()
        elif optiune == "2":
            x = input("Dati o pozitie: ")
            y = input("Dati un numar: ")
            numarRegasitDeLaoPozitieData(int(x), int(y), lst)
        elif optiune == "3":
            print(sumaTuturorNumerelorIntregi(lst))
        elif optiune == "4":
            print(numerePareDinLista(lst))
        elif optiune == "5":
            print(procesareLista(lst))
        elif optiune == "a":
            print(lst)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")


if __name__ == '__main__':
    main()