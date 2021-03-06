import math

'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(3, n // 2, 2):
        if n % i == 0:
            return False

    return True
    pass


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    s = 1
    for _ in lst:
        s *= _
    return s
    pass


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    while x is not y:
        if x > y:
            x -= y
        else:
            y -= x

    return x
    pass


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    while y != 0:
        rest = x % y
        x = y
        y = rest
    return x

    pass


# This is the main function
def main():
    n = int(input("Alegeti:\n1 -> Verificare nr prim.\n2 -> Produsul numerelor din lista.\n3 -> CMMDC V1.\n4 -> CMMDC V2.\n"))
    if n == 1:
        numar = int(input("Introduceti numarul."))
        print(is_prime(numar))
    elif n == 2:
        lungime_lista = int(input("Introduceti lungimea listei."))
        lista = []
        for _ in range(0, lungime_lista):
            numarul = int(input("Introduceti numarul: "))
            lista.append(numarul)
        print(get_product(lista))
    elif n == 3 or n == 4:
        primul_numar = int(input("Introduceti primul numar: "))
        al_doilea_numar = int(input("Introduceti al doilea numar: "))
        print(get_cmmdc_v1(primul_numar, al_doilea_numar))

    pass


if __name__ == '__main__':
    main()
