class Kütüphane:
    def __init__(self):
        self.dosya_adı = "books.txt"
        self.dosya = open(self.dosya_adı, "a+")
        self.dosya.seek(0)
        if not self.dosya.read():
            print(f"{self.dosya_adı} dosyası boş. Yeni dosya oluşturuluyor.")
            self.dosya.close()
            self.dosya = open(self.dosya_adı, "w+")

    def __del__(self):
        self.dosya.close()

    def kitapları_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        if not kitaplar:
            print("Kütüphane'nin içinde kitap yok")
        else:
            for satır, s in enumerate(kitaplar, start=1):
                b = s.strip().split(",")
                print(f"{satır}. Kitap Adı: {b[0]}, Yazarı: {b[1]}")

    def kitap_ekle(self):
        kitapAdı = input("Kitap Adı: ")
        yazar = input("Yazar Adı: ")
        yıl = input("Yayınlanma Tarihi: ")
        sayfa = input("Sayfa Sayısı: ")

        kitap_bilgisi = f"{kitapAdı},{yazar},{yıl},{sayfa}\n"
        self.dosya.write(kitap_bilgisi)
        print("Kitap Eklendi!")

    def kitap_sil(self):
        silinecek = input("Silinecek kitabın adını girin: ")

        with open(self.dosya_adı, "r") as dosya:
            kitaplar = dosya.readlines()

        bulundu = False
        with open(self.dosya_adı, "w") as dosya:
            for i, kitap in enumerate(kitaplar):
                if i == 0:
                    dosya.write(kitap)
                elif silinecek.lower() not in kitap.lower():
                    dosya.write(kitap)
                else:
                    bulundu = True

        if bulundu:
            print(f"'{silinecek}' adlı kitap silindi.")
        else:
            print(f"'{silinecek}' adlı kitap bulunamadı.")

def main():
    library = Kütüphane()

    while True:
        print("\n1. Kitapları Listele")
        print("2. Kitap Ekle")
        print("3. Kitap Sil")
        print("q. Çıkış")

        i = input("Seçimini yap: ")

        if i == "1":
            library.kitapları_listele()
        elif i == "2":
            library.kitap_ekle()
        elif i == "3":
            library.kitap_sil()
        elif i.lower() == "q":
            break
        else:
            print("Yanlış tuşa bastın. Tekrar dene.")


if __name__ == "__main__":
    main()
