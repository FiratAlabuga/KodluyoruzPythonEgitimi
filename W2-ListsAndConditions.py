x = [1, 2, 3]
y = [1, 2, 3]
# Identity Operator: is X==y x!=Y
#print(type(x))
print(x == y)
print(x is y)
print(x is not y) 
# Membership Operator: in
x = ['apple','banana']
print('greyfurt' in x) 
isim='tuğçe'
print('u' in isim) 

res=5<x<10 
x=8
# x, 5-10 arasında olan bir çift sayı mı?

result = ((x>5) and (x<10)) and (x%2==0)

print(result)

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1=float(input('Vize 1: '))
vize2=float(input('Vize 2: '))
final=float(input('Final: '))
average=((vize1+vize2)/2)*0.6 + (final * 0.4)
#result=(average>=50)and(final>=50)
result=(average>=50)or(final>=70)
print(f'Öğrencinin ortalaması:{average} ve geçme durumu {result}')

email = 'email@ornek.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())

print(f'Email bilgisi doğrumu: {isEmail} ve Parola doğru mu: {isPassword}') 

x, y, z = 2, 5, 10
print(y%x)
print(y//x)

num = int(input('sayı: '))

if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:
    print('sayı sıfır')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1=float(input('Vize 1: '))
vize2=float(input('Vize 2: '))
final=float(input('Final: '))
average=((vize1+vize2)/2)*0.6 + (final * 0.4)
#result=(average>=50)and(final>=50)
result=(average>=50)or(final>=70)

if(average>=50):
    if(final>50):
        print(f'öğrencinin ortalaması: {average} ve geçme durumu: başarılı')
    else:
        print(f'öğrencinin ortalaması: {average} ve geçme durumu: başarısız.Finalden en az 50 almalısın')
else:
    print(f'öğrencinin ortalaması: {average} ve geçme durumu: başarısız')

yazili1 = float(input('1.yazılı: '))
yazili2 = float(input('2.yazılı: '))
sozlu = float(input('sözlü: '))

ortalama = (yazili1 + yazili2 + sozlu)/3

if (ortalama>=0) and (ortalama<25):
     print(f'ortalamanız: {ortalama} notunuz: 0')
elif (ortalama >= 25 ) and (ortalama<45):
     print(f'ortalamanız: {ortalama} notunuz: 1')
elif (ortalama >= 45 ) and (ortalama<55):
     print(f'ortalamanız: {ortalama} notunuz: 2')
elif (ortalama >= 55 ) and (ortalama<70):
     print(f'ortalamanız: {ortalama} notunuz: 3')
elif (ortalama >= 70 ) and (ortalama<85):
     print(f'ortalamanız: {ortalama} notunuz: 4')
elif (ortalama >= 85 ) and (ortalama<=100):
     print(f'ortalamanız: {ortalama} notunuz: 5')
else:
     print('yanlış bilgi girdiniz.')

x=1
while x<=100:
    if x%2==1:
        print(f'sayı tek:{x}')
    else:
        print(f'sayi cifttir:{x}')
    x+=1
print("bitti") 

#key:value
products=[]
piece=int(input("Kaç Ürün Eklemek İstiyorsunuz ?"))
i=0
#name=" "
#price=" "
while(i<piece):
    name=input("Ürün Adı:")
    price=input("Ürünün Fiyatı")
    products.append({
        'name':name,
        'price':price
    })
    i+=1 
for product in products:
    print(f'Ürün Adı:{product['name']},Ürünün Fiyatı:{product['price']}')
