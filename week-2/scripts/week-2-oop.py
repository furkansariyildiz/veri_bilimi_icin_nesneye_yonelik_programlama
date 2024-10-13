#!/usr/bin/env python3


class Araba:
    """
    Araba sinifi
    """
    def __init__(self, marka: str, model: str):
        """
        Araba sinifinin yapicisi.

        Args:
            marka (str): Araba sinifinin markasi.
            model (str): Araba sinifinin modeli.
        """
        self.marka_ = marka
        self.model_ = model


    
    def bilgileriYazdir(self):
        """
        Araba bilgilerini yazdirma methodu.
        """
        print(f"Marka: {self.marka_}, Model: {self.model_}")



class Dikdortgen:
    """
    Dikdortgen sinifi
    """
    def __init__(self, genislik, yukseklik):
        """
        Dikdörtgen sinifinin yapicisi.

        Args:
            genislik (float): Dikdörtgenin genişliği.
            yukseklik (float): Dikdörtgenin yüksekliği.
        """
        self.genislik_ = genislik
        self.yukseklik_ = yukseklik

    

    def alanHesapla(self):
        """
        Dikdortgenin alanini hesaplayan fonksiyon
        """
        return self.genislik_ * self.yukseklik_



class Kare:
    """
    Kare sinifi
    """
    def __init__(self, kenar_uzunlugu):
        """
        Kare sinifinin yapicisi

        Args:
            kenar_uzunlugu (float): Karenin kenar uzunlugu
        """
        self.kenar_uzunlugu_ = kenar_uzunlugu



    def bilgileriYazdir(self):
        """
        @brief Karenin bir kenarini ekrana yazdirir.
        """
        print(f"Karenin kenar uzunlugu: {self.kenar_uzunlugu_}")



class HesapMakinesi:
    """
    Hesap Makinesi sinifi
    """
    def __init__(self, **kwargs):
        """
        Hesap Makinesi sinifinin yapicisi

        Args:
            **kwargs (dict): Parametrelerin alincagi parametre. Minimum 2 sayi, maksimum 3 sayi alabilir. Parametrelerin isimleri sirasiyla 'birinci_sayi', 'ikinci_sayi' ve 'ucuncu_sayi' olmalidir.
        """
        self.birinci_sayi_ = kwargs.get("birinci_sayi")
        self.ikinci_sayi_ = kwargs.get("ikinci_sayi")
        self.ucuncu_sayi_ = kwargs.get("ucuncu_sayi", None)



    def toplamaİslemi(self):
        """
        Toplama islemi yapan fonksiyon
        """
        if self.ucuncu_sayi_ == None:
            return self.birinci_sayi_ + self.ikinci_sayi_
        
        return self.birinci_sayi_ + self.ikinci_sayi_ + self.ucuncu_sayi_
    


class Merhaba:
    """
    Merhaba sinifi
    """
    def __init__(self):
        """
        Merhaba sinifinin yapicisi
        """
        print("Merhaba Dunya")




if __name__ == '__main__':
    # Question-1
    araba = Araba("Toyota", "Corolla")
    araba.bilgileriYazdir()

    # Question-2
    diktortgen = Dikdortgen(2, 3)
    print(f"Dikdortgenin alani: {diktortgen.alanHesapla()}")

    # Question-3
    kare = Kare(3)
    kare.bilgileriYazdir()

    # Question-4
    hesap_makinesi = HesapMakinesi(birinci_sayi=1, ikinci_sayi=3)
    print(f"Iki parametreli toplama islemi: {hesap_makinesi.toplamaİslemi()}")
    hesap_makinesi = HesapMakinesi(birinci_sayi=1, ikinci_sayi=2, ucuncu_sayi=3)
    print(f"Uc parametreli toplama islemi: {hesap_makinesi.toplamaİslemi()}")

    # Question-5
    merhaba = Merhaba()