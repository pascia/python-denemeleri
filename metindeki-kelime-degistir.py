while 194>5:#while true
    print("Bu program bir metin içindeki kelime1'leri kelime2'ye dönüştürür.")
    girdi = input("Lütfen değiştirilmesini istediğiniz kelimeyi yazınız (kelime1-kelime2): ")

    i=0
    while i<len(girdi): #girdinin her harfini tek tek kontrol et. "-" olduğu kısımdan ayır.
        if girdi[i]=="-":
            kelime1 = girdi[:i] # "-"nin sol kısmını kelime1 olarak kaydet
            kelime2 = girdi[i+1:] # "-"nin sağ kısmını kelime2 olarak kaydet
        i+=1

    metin = input("Lütfen metni giriniz:\n")
    i2=0
    cikis=""
    while i2<len(metin): #metinin her harfini kontrol ederek kelime1'i bulmaya çalış
        if metin[i2:i2+(len(kelime1))] == kelime1: # Eğer kelime1'in uzunluğu kadar kontrol ettiğimiz karakterler kelime1'e eşit ise
            cikis += metin[:i2]+kelime2 # Çıkışa kelime1'den önceki kısmı ve kelime2'yi ekle
            metin = metin[i2+(len(kelime1)):] # Bundan sonra kelime1'den sonraki kısmı tekrar tara
            i2 = -1 # başa dön
        elif i2==len(metin)-1: #Eğer metin tamamen kontrol edildiyse geri kalan metni çıkış'a ekle
            cikis += metin
        i2+=1

    print(cikis)
