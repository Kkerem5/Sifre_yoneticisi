import random

sifreler = {}
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    karar = input('Şifre oluşturmek için "s", kaydedilen şifrelere bakmak için "a" tuşuna basın, çıkmak için "cık" yazın: ')   

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
    elif karar == 'cık':
        break
    else:
        print("Geçersiz seçenek, lütfen 's', 'a' veya 'cık' girin.")
