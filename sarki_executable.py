from sarki_class_modul import *

bilgi_mesaji = """***********************************

Şarkı Veritabanı Programına Hoşgeldiniz.

İşlemler;

1. Şarkıları Göster

2. Şarkı Sorgula

3. Şarkı Ekle

4. Şarkı Silme

5. Toplam Şarkı Süresini Göster

Çıkmak için 'q' ya basın...
***********************************"""

print (bilgi_mesaji)

sarki_kutuphanesi = Sarki_Kutuphanesi()

while True:
    işlem = input("Yapacağınız İşlem: ")

    if (işlem == "q"):
        print(bilgi_mesaji)
        print("   "*3000)
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (işlem == "1"):
        print("   "*3000)
        print(bilgi_mesaji)
        sarki_kutuphanesi.sarkilari_goster()

    elif (işlem == "2"):
        print("   "*3000)
        print(bilgi_mesaji)
        isim = input("Hangi sarkiyi istiyorsunuz ? ")
        print("Sarki Sorgulanıyor...")

        sarki_kutuphanesi.sarki_sorgula(isim)

    elif (işlem == "3"):

        isim = input("İsim:")

        tur = input("Tür:")

        sanatci = input("Sanatçı:")

        sure = input("Süre:")

        # Burada herhangi bir stringi parçalarına ayıran bir fonksiyon kullanarak, kullanının sadece xy:bc formatında süre bilgisi girmesini sağlandı.
        format_kontrol = sure.split(":")
        def ayirici(kelime):
            return [char for char in kelime]

        ayrilmis_liste = ayirici(sure)

# ':' karakteri xx:ab formatında sadece bir kere geçmelidir. Bu yüzden bu for döngüsünde ':' karakterini sayıp
        karakter_sayisi = 0
        uygun = False
        for e in ayrilmis_liste:
            if len(ayrilmis_liste) == 5:
                if e == ':':
                    karakter_sayisi += 1

                if karakter_sayisi == 1:
                    uygun = True
                else:
                    uygun = False
            else:
                uygun == False

        if uygun == True:
            if len(format_kontrol) == 2: # xx:ab formatında girilen bir süre değeri, split(':') fonksiyonuyla en fazla 2 elemana sahip bir diziye dönüşür.
                        try:
                            format_kontrol[0] = int(format_kontrol[0]) #Eğer kullanıcı sayı yerine harf, karakter vb girerse tam sayıya çevrilemeyen bir değer olduğundan hata almadan doğru format istenir.
                            format_kontrol[1] = int(format_kontrol[1])

                            if format_kontrol[1] <= 59 and format_kontrol[0] <= 59:
                                print("   " * 3000)
                                print(bilgi_mesaji)
                                yeni_sarki = Sarki(isim, tur, sanatci, sure)
                                print("Sarki ekleniyor....")
                                print("")
                                time.sleep(2)
                                sarki_kutuphanesi.sarki_ekle(yeni_sarki)
                                print("Sarki Eklendi....")
                        except ValueError:
                            print("   " * 3000)
                            print(bilgi_mesaji)
                            print("Hatalı format girdiniz. xy:ab şeklinde süre bilgisi girin.")
            else:
                print("   "*3000)
                print(bilgi_mesaji)
                print("Hatalı format girdiniz. xy:ab şeklinde süre bilgisi girin.")
        else:
            print("   "*3000)
            print(bilgi_mesaji)
            print("Hatalı format girdiniz. xy:ab şeklinde süre bilgisi girin.")

#Kullanıcının süre formatını kontrol eden işlemlerin sonu.


    elif (işlem == "4"):
        print(bilgi_mesaji)
        isim = input("\nHangi şarkıyı silmek istiyorsunuz ?\n")

        cevap = input("Emin misiniz ? (E/H)\n")
        if (cevap == "E"):
            print("   "*3000)
            print(bilgi_mesaji)
            sarki_kutuphanesi.sarki_sil(isim)

    elif (işlem == "5"):
        print("   "*3000)
        print(bilgi_mesaji)
        sarki_kutuphanesi.toplam_sure()

    else:
        print("   "*3000)
        print(bilgi_mesaji)
        print("Geçersiz İşlem...\n")
