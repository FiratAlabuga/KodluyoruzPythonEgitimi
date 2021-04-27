#global scope
x='global x'

def func():
    #local scope
    x='local x'
    print(x)

func()
print(x) 


isim='Tülin'

def degisIsim(yeni_isim):
    global isim
    isim=yeni_isim
    print(isim)

degisIsim('Tuğçe')
print(isim)

def square(num):
    return num ** 2

print(square(6))


square=lambda num:num ** 2
print(square)


TulinHesap={
    'adsoyad':' Tülin Kışlak',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}
MelekHesap={
    'adsoyad':' Melek Baydoğan',
    'hesapNo': '13245678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paracekme(hesap,miktar):
    print(f"Merhaba {hesap['adsoyad']}")
    if(hesap['bakiye']>=miktar):
        hesap['bakiye']-= miktar
        print("Paranızı Alabilirsiniz.")
        bakiyem(hesap)
    else:
        toplam_bakiye=hesap['bakiye']+hesap['ekHesap']
        
        if(toplam_bakiye>=miktar):
            ekHesapKullanilsinmi=input('Ek hesap kullanmak istiyor musunuz ? (e/h)')
            if ekHesapKullanilsinmi=='e':
                ekHesapKullanilacakMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                print("Paranızı Alabilirsiniz.")
                bakiyem(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmamaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyem(hesap)

def bakiyem(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paracekme(TulinHesap,3000)
paracekme(TulinHesap,1700)

class Dizi():
    def __init__(self,diziAd,diziYonetmen,diziZaman):
        self.diziAd=diziAd
        self.diziYonetmen=diziYonetmen
        self.diziZaman=diziZaman
    def __str__(self):
        return f"{self.diziAd} by {self.diziYonetmen}"
    def __del__(self):
        print('film objesi silindi')

dizi=Dizi('The 100','....',50) 

class Circle:
    #class object attribute
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    def cevrehesap(self):
        return 2*self.pi*self.yaricap
    def alanhesap(self):
        return self.pi*(self.yaricap**2)

c1=Circle()
c2=Circle(5)
print(f'c1:alan={c1.alanhesap()} çevre={c1.cevrehesap()}')
print(f'c2:alan={c2.alanhesap()} çevre={c2.cevrehesap()}') 
 
class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

p1=Person('Tülin','Kışlak')
print(p1.firstName + ' ' + p1.lastName)

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.number=number
        print('Student Created')
    def who_am_i(self):
        print('I am a Student')
    def merhaba(self):
        print('Hello I am a Student')

s1=Student('Mehmet','Bülbül',134)
print(s1.firstName + ' ' + s1.lastName+ ' '+ str(s1.number))
s1.merhaba()
s1.who_am_i() 
#OOP 