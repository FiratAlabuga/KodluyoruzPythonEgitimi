#print(a)=>NameError
#int('1a2')=>ValueError
#print('tuğç'e)=>SyntaxError
try:
    x=int(input('x: '))
    y=int(input('y: '))
    print(x/y)
except(ZeroDivisionError,ValueError) as e:
    #print(f'hata:{0}',e)
    print('hata')
    print(e) 


while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz', ex)
    else:
        break
    finally:
        print('try except sonlandı.')

def fact(x):
    x=int(x)
    if x<0:
        raise ValueError('Negatif Değer')
    result=1
    for i in range(1,x+1):
        result *=i
    return result
for x in [5,10,20,-3,'10a']:
    try:
        y=fact(x)
    except ValueError as e:
        print(e)
        continue
    print(y) 

import math
#from math import factorial

print(math.factorial(5))





html_doc = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>

    <h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""

from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,'html.parser')
#result=soup.prettify()
result=soup.title
print(result)
print(soup.h2)
print(soup.h2.name)
print(soup.h2.string)
print(soup.find_all('h2'))
print(soup.findAll('h2')[1])
print(soup.find_all('div')[2].ul.find_all('li'))
print(soup.find_all('a'))
import requests
import json

allfetch=requests.get("https://jsonplaceholder.typicode.com/photos")
allfetch=json.loads(allfetch.text)
for i in allfetch:
    if i['id']==4:
        print(i['title'])
        print(i['url'])
print(type(allfetch)) 


import requests
from bs4 import BeautifulSoup

url='https://www.imdb.com/chart/top?ref_=nv_mv_250'
allfetch=requests.get(url).content
soup=BeautifulSoup(allfetch,'html.parser')
a=[]
a=soup.find('tbody',{'class':'lister-list'}).find_all('tr',limit=50)
count=1
for i in a:
    title=i.find('td',{'class':'titleColumn'}).find('a').text
    year=i.find('td',{'class':'titleColumn'}).find('span').text.strip('()')
    rating=i.find('td',{'class':'ratingColumn imdbRating'}).find('strong').text
    print(f'{count}-Filmin Adı:{title},Yıl:{year},Rating:{rating}')
    count+=1