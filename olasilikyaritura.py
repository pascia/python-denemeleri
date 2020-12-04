import random
sum=0
tekrar = 0
tekrarlar = []
enbuyuk = 0
enbuyugu = 0

for i in range(10**7):
    sayi = random.sample([True,False],1)
    if sayi[0]:
        tekrar += 1
    else:
        if not tekrar == 0:
            tekrarlar.append(tekrar)
        tekrar=0
    if i%100000==0:
        print(str(i)+","+str(sayi[0]))

for i in range(len(tekrarlar)):
    sum+=tekrarlar[i]
    if tekrarlar[i] >= enbuyuk:
        enbuyuk = tekrarlar[i]
        enbuyugu = i
        
    
print(sum/len(tekrarlar))
print(enbuyuk)
print(tekrarlar[enbuyugu])