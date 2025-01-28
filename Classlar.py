# Hesap makinesi sınıfı
class calculator():
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2
    def cikart(self):
        return self.sayi1 - self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2

hesapMakinesi=calculator(64,11)
print(hesapMakinesi.bol())
print(hesapMakinesi.carp())
print(hesapMakinesi.cikart())
print(hesapMakinesi.topla())  

# Öğrenci sınıfı
class Ogrenci():
    def __init__(self,ad,notlar,sinif):
        self.ad=ad
        self.notlar=notlar
        self.sinif=sinif
    def ortNot(self):
        return (sum(self.notlar)/len(self.notlar))
ogrenci=Ogrenci("Emre",[50,70,100,95,57],2)
print(ogrenci.ortNot())
print(ogrenci.ad)
print(ogrenci.sinif)
print(ogrenci.notlar)

# Kalıtım
# Hayvan sınıfı
class Hayvan():
    def __init__(self):
        print("Hayvan sınıfı init çağırıldı")
    def sesCikar(self):
        print("Hayvan sınıfının ses çıkar fonksiyonu çağırıldı.")

class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("Kedi sınıfı init çağırıldı")
    def sesCikar(self):
        print("Miyav")

class Kopek(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("Köpek sınıfı init çağırıldı")
    def sesCikar(self):
        print("Hav Hav")
hayvan=Hayvan()
hayvan.sesCikar()
kedi=Kedi()
kedi.sesCikar()
kopek=Kopek()
kopek.sesCikar()

# Araba sınıfı
class Araba():
    def __init__(self):
        print("Araba sınıfı init çağırıldı.")
class ElektrikliAraba(Araba):
    def __init__(self):
        Araba.__init__(self)
    def pilSeviyesi(self):
        print("Pil seviyesi gösteriliyor.")
    def sarjEt(self):
        print("Araba şarj ediliyor.")
araba=Araba()
elektrikliAraba=ElektrikliAraba()
elektrikliAraba.pilSeviyesi()
elektrikliAraba.sarjEt()

# Özel metotlar
# __add__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Toplama işlemi yalnızca başka bir Vector ile yapılabilir.")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2
print(v3)  

# __str__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Toplama işlemi yalnızca başka bir Vector ile yapılabilir.")

    def __str__(self):
        return f"Vektör: ({self.x}, {self.y})"

v = Vector(3, 4)

print(v)  


        
