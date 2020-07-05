while 1==1:
    girissayisi = int(input("Bir sayı girin, 16'lı sisteme dönüştürelim"))
    alfabe = "ABCDEF"
    cikissayisi = ""

    while girissayisi != 0:
        if (girissayisi%16 >= 10): # Sayıyı 16'ya böl. Kalanı en sağa satıra yaz.
            cikissayisi = alfabe[(girissayisi%16)-10] + cikissayisi #Kalan 9'dan fazla ise alfabe'deki bir harfi kullan.
        else: #Kalan 9'dan az ise, doğrudan çıkış sayısı'nın başına ekle (burası deneme yazısım)
            cikissayisi = str(girissayisi%16)+cikissayisi
        girissayisi//=16 # Her şekilde sayıyı 16'ya kalansız böl. Bir sonraki işlemde tekrar kullan

    print("Sayınız çevrildi:", cikissayisi)
