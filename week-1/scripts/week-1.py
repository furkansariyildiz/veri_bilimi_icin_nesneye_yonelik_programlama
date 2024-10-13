#!/usr/bin/env python3

from typing import overload
import rclpy
import random
import time

class Week1:
    def __init__(self):
        pass

    @overload
    def topla(self, a: int, b: int) -> int:
        ...

    @overload
    def topla(self, a: list) -> int:
        ...

    def topla(self, a, b=None):
        if isinstance(a, list):
            return sum(a)
        elif isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            raise ValueError("Geçersiz parametreler. Ya iki sayı ya da bir liste bekleniyor.")

    def pageFour(self):
        """
        @brief Check alphabets of name is upper or lower via for loop.
        @param name (str) Name which will be controlled.
        @returns void
        """
        print("furkan")
        print("furkan", "sariyildiz", "T", "B", "M", "M", sep='.')

        a = "ali"
        b = 5

        print(type(a))
        print(type(b))

        liste1=[1,3,3,5,4,5,4,"ali","canan"]
        liste1[0]
        print(len(liste1)) 
        print(dir(liste1)) 
        liste2=[1,3,3,5,4,5,4]
        liste2.sort()
        liste2
        liste2[0]=100000 
        liste2[0]
        liste2
        liste2.pop()
        liste2.append(25)
        liste2.insert(7,"25")
        print(liste2)
        print(liste2[7])
        demet=("ali","ayşe")
        print(demet)
        print(len(demet))
        print(demet[0])
        print(dir(demet))
    

    def pageFive(self):
        x = "FUrkan"
        print(type(x))

        print(x.capitalize())

        print(self.topla([1, 2, 3]))  # Çıktı: 6
        print(self.topla(1, 2))       # Çıktı: 3


    def pageSix(self):
        liste1=[1,2,3,4,5]
        liste1 
        print("Liste1: {}".format(liste1))
        liste2=[i*2 for i in liste1]
        print("Liste2: {}".format(liste2))


    def pageEight(self):
        rastgele = random.randint(1, 100)
        tahmin_hakki = 5

        while True:
            tahmin = int(input("tahmini gir 1-100: " ))
            
            if tahmin == rastgele:
                time.sleep(1)
                print("ok")
                break

            elif tahmin < rastgele:
                tahmin_hakki = tahmin_hakki - 1
                print("sayiyi buyult")

            elif tahmin > rastgele:
                tahmin_hakki = tahmin_hakki - 1
                print("sayiyi kucult")

            else:
                print("1-100 arasinda deger gir.")

            if tahmin_hakki == 0:
                print("hakkiniz bitti.")
                break


if __name__ == '__main__':
    week1 = Week1()

    week1.pageFour()
    week1.pageFive()
    week1.pageSix()
    week1.pageEight()