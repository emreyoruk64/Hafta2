# Bir sayı dizisinin ortalamasını hesaplayan metot
def ortHesapla(liste):
    toplam=sum(liste)
    print("Dizinin ortalaması:",(toplam/len(liste)))
ortHesapla([1,2,3,4,5])
ortHesapla([25,41,58,64,81,11])

# Girilen 2 sayının en büyüğünü döndüren fonksiyon
def enBuyuk():
    sayi1=int(input("1. sayiyi giriniz:"))
    sayi2=int(input("2. sayiyi giriniz:"))
    if sayi1>sayi2:
        return sayi1
    elif sayi2>sayi1:
        return sayi2
print(enBuyuk())

# Bir metin içindeki kelimeleri sayan fonksiyon
def kelimeSay():
    toplam=0
    metin=str(input("Bir metin giriniz:"))
    kelimeler=metin.split()
    toplam=len(kelimeler)
    print("Kelime sayısı:",toplam)
kelimeSay()

# Lambda , filter ve map
# Map
dizi = [1, 2, 3, 4, 5]

def karesiniAl(sayi):
    if sayi % 2 != 0:
        return sayi * sayi
    return sayi

yeniListe = list(map(karesiniAl, dizi))
print(yeniListe)

# Filter
def ciftMi(number):
    return number%2==0
    
print(list(filter(ciftMi,list(range(0,50)))))

# Lambda 
topla = lambda x, y: sum(range(min(x, y), max(x, y) + 1))

print(topla(15,21))  

# Global ve yerel değişkenlerle çalışan bir uygulama 
sonuc=1

def faktoriyel():
    global sonuc
    a=int(input("Bir sayı giriniz:"))
    for i in range(1,a+1):
        sonuc*=i
    return sonuc
print(faktoriyel())

        