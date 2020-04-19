import sqlite3
import math
import time

class Sarki():

    def __init__(self,isim,tur,sanatci,sure):

        self.isim = isim
        self.tur = tur
        self.sanatci = sanatci
        self.sure = sure

    def __str__(self):
        return "Şarkının Adı: {}\nTürü: {}\nSanatçı: {}\nSüre: {}\n****************************\n".format(self.isim,self.tur,self.sanatci,self.sure)

class Sarki_Kutuphanesi():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarki_kutuphanesi.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create table if not exists sarkilar (İsim TEXT, Tür TEXT, Sanatçı TEXT, Süre TEXT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):

        self.baglanti.close()

    def sarkilari_goster(self):

        sorgu = "Select * from sarkilar"

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):

            print("Şarkı bulunamadı.")

        else:
            for x in sarkilar:
                sarki = Sarki(x[0],x[1],x[2],x[3])
                print(sarki)

    def sarki_sorgula(self,isim):
        sorgu = "Select * from sarkilar where İsim = ?"
        self.cursor.execute(sorgu,(isim,))

        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Böyle bir şarkı bulunmuyor.")
        else:
            sarki = Sarki(sarkilar[0][0],sarkilar[0][1],sarkilar[0][2],sarkilar[0][3])

            print(sarki)

    def sarki_ekle(self, sarki):

        sorgu = "Insert into sarkilar Values(?,?,?,?)"

        self.cursor.execute(sorgu,(sarki.isim,sarki.tur,sarki.sanatci,sarki.sure))
        self.baglanti.commit()

    def sarki_sil(self, isim):

        sorgu1 = "Delete from sarkilar where İsim = ?"

        sorgu2 = "Select * from sarkilar where İsim = ?"

        self.cursor.execute(sorgu2,(isim,))
        sarki = self.cursor.fetchall()

        if( len(sarki)== 0):
            print("Böyle bir şarkı bulunmuyor.")
        else:
            self.cursor.execute(sorgu1,(isim,))
            print("{} İsimli şarkı başarıyla silindi.".format(isim))
        self.baglanti.commit()

    def toplam_sure(self):
        sorgu = "Select * from sarkilar"

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()
        toplam_sure = 0
        i = 0
        dakika = 0

        if (len(sarkilar) == 0):

            print("Şarkı bulunmadığı için toplam şarkı süresi hesaplanamadı.")

        else:
            for x in sarkilar:
                suresi = int(sarkilar[i][3].split(":")[0]) * 60 + int(sarkilar[i][3].split(":")[1])

                toplam_sure += suresi
                i += 1
                dakika = toplam_sure/60
            print("Şarkı veritabanında {} adet şarkı bulunmaktadır ve toplam süresi {} dakika {} saniyedir.".format(i,math.floor(dakika),toplam_sure - math.floor(dakika)*60))














