sira=10
a=1
for i in range(0,sira):
    prin = "Basamak:  "
    bosluk = sira-i
    kare = i+1
    while bosluk != 0:
        prin+=" "
        bosluk-=1
    while a <= 2:
        while kare != 0:
            prin+="#"
            kare-=1
        else:
            prin += " "
            a+=1
            kare = i+1
    a=1
    print(prin)
