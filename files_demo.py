def notHesapla(satir):
    satir = satir[:-1] #aradaki boşlukları aldık
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not2) / 3

    if ortalama > 90 and ortalama <= 100:
        harf = 'AA'
    elif ortalama >= 85 and ortalama <=89:
        harf = 'BA'
    elif ortalama >= 65:
        harf = 'CC'
    else: 
        harf = 'FF'

    return ogrenciAdi + ":" + harf + "\n"

def ortalamalariOku():
    with open("sinavNotlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(notHesapla(satir))

    
def notGir():
    ad = input('Öğrenci adı : ')
    soyad = input('Öğrenci soyad : ')
    not1 = input('not 1 : ')
    not2 = input('not 2 : ')
    not3 = input('not 3 : ')

    with open("sinavNotlari.txt","a",encoding="utf-8") as file:
        file.write(ad + ' '  + soyad + ':' + not1 + ','+ not2 + ',' + not3 + '\n')

def notlariKayitEt():
    with open("sinavNotlari.txt","r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(notHesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as  file2:
            for i in liste:
                file2.write(i)




while True:
    islem = input('1- Notları Oku\n2- Not Gir\n3- Notları Kaydet\n4- Çıkış\n')

    if islem == "1":
        ortalamalariOku()
    elif islem == "2":
        notGir()
    elif islem == "3":
        notlariKayitEt()
    else:
        break