from sarki_class_modul import *

print("""***********************************

Şarkı Veritabanı Programına Hoşgeldiniz.

İşlemler;

1. Şarkıları Göster

2. Şarkı Sorgulama

3. Şarkı Ekle

4. Şarkı Sil

6. Toplam Şarkı Süresini Göster

Çıkmak için 'q' ya basın...
***********************************""")

sarki_kutuphanesi = Sarki_Kutuphanesi()

while True:
    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (işlem == "1"):
        print("****************************")
        sarki_kutuphanesi.sarkilari_goster()

    elif (işlem == "2"):
        isim = input("Hangi sarkiyi istiyorsunuz ? ")
        print("Sarki Sorgulanıyor...")


        sarki_kutuphanesi.sarki_sorgula(isim)

    elif (işlem == "3"):
        isim = input("İsim:")
        tur = input("Tür:")
        sanatci = input("Sanatçı:")
        sure = input("Süre:")
        format_kontrol = sure.split(":")

        def ayirici(kelime):
            return [char for char in kelime]

        ayrilmis_liste = ayirici(sure)


        sayac = 0
        onay = False
        for e in ayrilmis_liste:
            if len(ayrilmis_liste) == 5:
                if e == ':':
                    sayac += 1

                if sayac == 1:
                    onay = True
                else:
                    onay = False
            else:
                onay == False





        if onay == True:
            if len(format_kontrol) == 2:
                        try:
                            format_kontrol[0] = int(format_kontrol[0])
                            format_kontrol[1] = int(format_kontrol[1])

                            if format_kontrol[1] <= 59 and format_kontrol[0] <= 59:
                                yeni_sarki = Sarki(isim, tur, sanatci, sure)
                                print("Sarki ekleniyor....")
                                time.sleep(2)
                                sarki_kutuphanesi.sarki_ekle(yeni_sarki)
                                print("Sarki Eklendi....")
                        except ValueError:
                            print("Hatalı format girdiniz XX:YY")
            else:
                print("Hatalı Format")
        else:
            print("Hatalı format girdiniz. Formatı XX:YY Şeklinde giriniz.")


    elif (işlem == "4"):
        isim = input("\nHangi şarkıyı silmek istiyorsunuz ?\n")

        cevap = input("Emin misiniz ? (E/H)\n")
        if (cevap == "E"):
            time.sleep(2)
            sarki_kutuphanesi.sarki_sil(isim)

    elif (işlem == "5"):

        sarki_kutuphanesi.toplam_sure()

    else:
        print("Geçersiz İşlem...\n")
