"""
# 1- Çarpim tablosu hazirlayiniz.

for i in range(1,11):
     print('*************')
     for k in range(1,11):
         print("{} x {} = {}".format(i,k,i*k))
"""
"""
# Rastgele bir sayıyı tahmin etmek
import random
sayi = random.randint(1,10)
hak = 5
sayac = 0

while hak > 0 :
    hak -=1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz.')
        break
    elif sayi > tahmin:
        print('yukari')
    else:
        print('aşaği')
    
    if hak == 0:
        print(f'hakkiniz bitti.Tutulan sayi : {sayi}')
"""
