def wpisywanie_hasla():
    password = None
    while password != "854":
        password = input("Wpisz hasło: ")
    print("Kod zaakceptowany")


def pole_kwardratu():
    a = float(input("Podaj a: "))
    p = a * a
    return p


def dec_to_bin():
    d = int(input("Podaj liczbę całkowitą większa od 0: "))
    binary_string = ""
    while d != 0:
        r = d % 2
        if r == 1:
            binary_string = '1' + binary_string
        else:
            binary_string = '0' + binary_string
        d = d // 2
    return binary_string


if __name__ == '__main__':
    print(dec_to_bin())
