def wpisywanie_hasla():
    password = None
    while password != "854":
        password = input("Wpisz hasło: ")
    print("Kod zaakceptowany")


def pole_kwardratu():
    a = float(input("Podaj a: "))
    p = a * a
    return p


if __name__ == '__main__':
    wpisywanie_hasla()
