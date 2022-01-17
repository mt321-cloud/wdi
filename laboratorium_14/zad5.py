# Zadanie 5.
# Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
import unittest
import pytest


def test_file1_method1():
    assert int(n) % 2 == 0, "liczba jest nieparzysta"
    # assert x == y, "test failed"


def test_file1_method2():
    assert n_bin[-1] == '0',  "liczba jest nieparzysta"


# test_file1method1()


# class SimpleTest(unittest.TestCase):

#     # Returns True or False.
#     def test_n_less(self):
#         self.assertLessEqual(int(n), 100)

#     def test_n_not_equal_bin(self):
#         self.assertEqual(int(n_bin), int(n), 'Nie sa rowne')


def czy_palindrom(liczba):
    i = 0
    while i < len(liczba)/2:
        if liczba[i] != liczba[-i-1]:
            return False
        i += 1
    return True


class NegativeValue(Exception):
    pass


while True:
    n = input('Podaj liczbe naturalna:')
    try:
        if int(n) < 0:
            raise NegativeValue
        else:
            break
    except ValueError:
        print("Podana wartosc nie jest liczba. Sproboj ponownie")
    except NegativeValue:
        print("Podana liczba nie jest liczba naturalna. Sprobuj ponownie")


n_bin = bin(int(n))[2:]
print('W systemie binarnym:', n_bin)

# unittest.main()

if czy_palindrom(n):
    print('Podana liczba jest palindromem w systemie dziesietnym')
else:
    print('Podana liczba nie jest palindromem w systemie dziesietnym')

if czy_palindrom(n_bin):
    print('Podana liczba jest palindromem w systemie binarnym')
else:
    print('Podana liczba nie jest palindromem w systemie binarnym')
