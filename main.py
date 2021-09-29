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

    for i in range(3, int(math.sqrt(n)), 2):
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
    while x != y:
        if x > y:
            y -= x
        else:
            x -= y

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


def main():
    pass


if __name__ == '__main__':
    main()
