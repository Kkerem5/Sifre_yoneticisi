import random

sifreler = {}
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    karar = input('Şifre oluşturmek için "s", kaydedilen şifrelere bakmak için "a",kaydedilen şifreleri ayarlamak için "f" tuşuna basın. çıkmak için "cık" yazın:')   

    if karar == 's': 
        while True:
            sifre_uzunlugu= int(input("Şifren kaç harfli olsun?\n"))
            sifre = ""
            
            for i in range(sifre_uzunlugu):
                sifre = sifre + random.choice(karakterler)
            print(sifre)

            sifre_kaydet = input('Şifrenizi kaydetmek için "k" tuşuna basın, değiştirmek için "d" tuşuna basın')
            if sifre_kaydet == 'k':
                platform = input('Neyin şifresi? ')
                sifreler[platform] = sifre
                print(sifreler)
                break
            elif sifre_kaydet == 'd':
                pass
            print('sifre')
    elif karar == 'a':
        print(sifreler)
    elif karar == 'f':
        while True:
            if len(sifreler) == 0:
                print('Kaydedilmiş şifre bulunamaktadır, çıkılıyor')
                break
            else:
                while True:
                    ayar_secimi = input('Bir "platform - şifreyi" silmek için "s", şifre değiştirmek için "d" tuşuna basınız, çıkmak için "cık"')
                    if ayar_secimi == 's':
                        print(sifreler)
                        hangisi = input('Girmek istediğiniz platform ve şifrenin platformunu girin:')
                        if hangisi in sifreler:
                            del sifreler[hangisi]
                            print('Güncel hali:', sifreler)
                        elif hangisi == 'cık':
                            break
                        else:
                            print('Girdiğiniz platform bulunamadı')
                    elif ayar_secimi == 'd':
                        while True:
                            de_platform = input('Hangi platfromun şifresini değiştirmek istiyorsunuz?, çıkmak için "cık"')
                            if de_platform in sifreler:
                                yeni_sifre_karar = input('Şifresini kendiniz değiştirmek için "a", otomatik bir şifre için "d" ye basınız')
                                if yeni_sifre_karar == 'a':
                                    yeni_sifre = input("Yeni şifrenizi girin:")
                                    sifreler[de_platform] = yeni_sifre
                                elif yeni_sifre_karar == 'd':
                                    yeni_uzunluk = int(input('Şifrenizin uzunluğu kaç olsun?'))
                                    for i in range(yeni_uzunluk):
                                        yeni_bir_sifre = sifre + random.choice(karakterler)
                                    print(yeni_bir_sifre)
                                    sifreler[de_platform] = yeni_bir_sifre
                                    print(sifreler)
                            elif de_platform == 'cık':
                                break
                    elif ayar_secimi == 'cık':
                        break
    elif karar == 'cık':
        break
    else:
        print("Geçersiz seçenek, lütfen 's', 'a' veya 'cık' girin.")
