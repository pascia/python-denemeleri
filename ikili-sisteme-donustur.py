while 1==1:
    decimal = int(input("Bir sayı yazın ikili sisteme dönüştürelim: "))
    binary = ""
    kalan = decimal
    k = 1
    i = 64
    ilkbir = 0
    while kalan != 0:
        k = 1
        kare = 0
        while kare != i+1:
            k *= 2
            kare += 1
        if (ilkbir==1 and kalan-k < 0):
            binary += "0"
        if (kalan - k >= 0):
            kalan = kalan-k
            binary += "1"
            ilkbir = 1
        if (kalan==0):
            binary += ("0"*(i+1))
        i -= 1
        while (len(binary) % 4 != 0):
            binary = "0" + binary

        while (binary[0:4]=="0000"):
            binary = binary[4:]


    print(binary)
