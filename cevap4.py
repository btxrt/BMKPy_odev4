# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.


def kelimeyi_tekrarla(kelime, tekrar_sayisi):
    for _ in range(tekrar_sayisi):
        print(kelime)

kelimeyi_tekrarla("Merhaba", 3)

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def dikdortgeninAlanı(uzun_kenar_uzunlugu,kısa_kenar_uzunluğu):
    print(uzun_kenar_uzunlugu*kısa_kenar_uzunluğu)
dikdortgeninAlanı(5,6)


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
import random

def yazi_tura():
    sayi = random.randint(0, 1)
    if sayi == 0:
        return "Yazı"
    else:
        return "Tura"

sonuc = yazi_tura()
print("Sonuç:", sonuc)


# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asal_sayilar(baslangic, bitis):
    asal_sayilar = []
    for sayi in range(baslangic, bitis + 1):
        if all(sayi % i != 0 for i in range(2, int(sayi**0.5) + 1)):
            asal_sayilar.append(sayi)
    return asal_sayilar

baslangic = 2
bitis = 5
sonuc = asal_sayilar(baslangic, bitis)
print(sonuc)
    
# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tam_bolenler(sayi):
    bolenler = []
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            bolenler.append(i)
    return bolenler

sayi = 8
sonuc = tam_bolenler(sayi)
print(sonuc)  