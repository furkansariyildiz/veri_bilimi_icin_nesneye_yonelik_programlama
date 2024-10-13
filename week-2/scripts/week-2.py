#!/usr/bin/env python3


from typing import Union



class Week2:
    def __init__(self):
        pass

    
    def question1(self, number_of_elements: int):
        """
        @brief Getting numbers from user via number of elements parameter and print.
        @param number_of_elements (int) Upper limit for list.
        """
        self.list_ = list()
        for i in range(0, number_of_elements):
            self.list_.append(int(input("Enter a number: ")))

        for count, number in enumerate(self.list_):
            print("array[" + str(count) + "]: " + str(number))



    def question2(self, number_of_elements: int):
        """
        @brief Getting stings from user via number of elements parameter and print.
        @param number_of_elements (int) Upper limit for list.
        """
        self.list_ = list()
        self.tupple_ = tuple()

        for i in range(0, number_of_elements):
            self.list_.append(str(input("Enter a string: ")))

        for count, string in enumerate(self.list_):
            self.tupple_ = self.tupple_ + (string, )

        print("Tupple: " + str(self.tupple_))



    def question3(self, checked_list: list):
        """
        @brief This function takes list and prints first and list items of list.
        @param checked_list (list) A list which will be printed by this function.
        """
        print("First item: " + str(checked_list[0]))
        print("List item: " + str(checked_list[-1]))



    def question4(self, checked_tuple: tuple):
        """
        @brief This function takes tuple and prints all elements from tuple.
        @param checked_tuple (tuple) A tuple which will be printed by this function.
        """
        for element in checked_tuple:
            print("Tupple element: " + str(element))



    def question5(self, list_for_adding_process: list, element: Union[str, int, float]):
        """
        @brief Adding element to list_for_adding_process list.
        @param list_for_adding_process (list) A list for adding element.
        @param element (Union[str, int, float]) An element for adding to list.
        """
        list_for_adding_process.append(element)
        
        print(str(list_for_adding_process[-1]) + " is added to list: " + str(list_for_adding_process))


    def isimYasListesi(self):
        liste = []
        for i in range(5):
            isim = input("İsim: ")
            yas = int(input("Yaş: "))
            kisi = (isim, yas)
            liste.append(kisi)
            sirali_liste = sorted(liste, key=lambda x: x[1])
            print("Yaşa göre sıralı liste: ", sirali_liste)



    def listeHesaplamalari(self):
        liste = list(map(int, input("input: ").split()))
        toplam = sum(liste)
        en_kucuk = min(liste)
        en_buyuk = max(liste)
        ortalama = toplam / len(liste)

        print(f"Toplam: {toplam}, En kucuk: {en_kucuk}, En buyuk: {en_buyuk}, Ortalama: {ortalama}")


if __name__ == '__main__':
    week2 = Week2()

    # Question-1
    week2.question1(number_of_elements=5)

    # Question-2
    week2.question2(number_of_elements=3)

    # Question-3
    question3_list = ["1", "2", "3", "4"]
    week2.question3(checked_list=question3_list)

    # Question-4
    question4_tuple = ("Istanbul", "Medeniyet", "University", 2024)
    week2.question4(checked_tuple=question4_tuple)

    # Question-5
    question5_list = ["1", "2", 3, "5"]
    week2.question5(list_for_adding_process=question5_list, element="Medeniyet")

    week2.isimYasListesi()
    
    week2.listeHesaplamalari()