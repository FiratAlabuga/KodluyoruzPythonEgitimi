import requests
from bs4 import BeautifulSoup

uri="https://www.n11.com/televizyon-ve-ses-sistemleri/televizyon"
html=requests.get(uri).content
soup=BeautifulSoup(html,"html.parser")
list=soup.find_all("li",{"class":"column"})
for i in list:
    urunBaslik=i.div.a.h3.text.strip()
    urunLink=i.div.a.get("href")
    urunEskiFiyat=i.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    urunYeniFiyat=i.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")
    print(f"UrunAdı:{urunBaslik},UrunLink:{urunLink},EskiFiyat:{urunEskiFiyat},YeniFiyat:{urunYeniFiyat}")

#------------------------------------------NUMPY----------------------------------------
import numpy as np

normalListe=[1,2,3,4,5]
numpyListe=np.array([1,2,3,4,5])
numpyListe2=np.array([1,2,3,4,5,6,7,8,9])
print(type(normalListe))
print(type(numpyListe))
normalUcBoyut=[[1,2,3],[4,5,6],[7,8,9]]
numpyUcBoyut=numpyListe2.reshape(3,3)
print(normalUcBoyut)
print(numpyUcBoyut)
print(numpyListe2.ndim)
print(numpyUcBoyut.ndim)
print(numpyListe2.shape)
print(numpyUcBoyut.shape)

print(numpyListe2[5])
print(numpyListe2[-1])
print(numpyListe2[0:3])
print(numpyListe2[:3])
print(numpyListe2[3:])
print(numpyListe2[::-1])
print(numpyUcBoyut[:,0:2])#tüm matrisi gezer,kaç tane alacağına karar verir. 

arrayOne=np.arange(0,10)
print(arrayOne)
arrayTwo=arrayOne.copy()
print(arrayTwo)
arrayTwo[0]=11
print(arrayTwo)
sifirDizisi=np.zeros(10)
print(sifirDizisi)
birDizisi=np.ones(10)
print(birDizisi)
diziEsitAralik=np.linspace(0, 100,5)
print(diziEsitAralik)
random=np.random.randint(10,20,5)
print(random)
randomMatris=np.random.randint(5,10,9).reshape(3,3)
print(randomMatris)
satirToplam=randomMatris.sum(axis=1)
print(satirToplam)
sutunToplam=randomMatris.sum(axis=0)
print(sutunToplam)
print(randomMatris.mean()) 






