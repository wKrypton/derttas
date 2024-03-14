while True:
    x = input("Merhaba Yakup, sorununu açıklar mısın? Seçenekler: aşk, stres, yalnızlık, motivasyon, bunalma: ")
    print("Tamamdır.")

    if x == "aşk":
        print("Olm unut artık onu, öyle biri yok, o çoktan seni unuttu, umrunda bile değilsin. Yapma böyle, kendini üzme boşuna")
    elif x == "stres":
        print("Streslenme boşuna, stresin kendini kontrol etmesine izin verme, sen onu kontrol et, unutma fazla stres seni boğacaktır o yüzden kendine mukayet ol ve iyi şeyler düşün.")
    elif x == "yalnızlık":
        print("Zirve tek kişilik dostum, unutma hedefler ciddileştikçe çevren azalır, birkaç gerçek dostta yeter, tek başına da yetersin, Sahte kişiliklere hacet ve yer yok. Bu seni yıldırmasın adamım kendine gel...")
    elif x == "motivasyon":
        print("Motivasyon mu istiyorsun? O zaman senin yerine seçtiği çocuğu ve arkandan konuşanların bir gün pişman olacağını düşün, onlara inat pes etme...")
    elif x == "bunalma":
        print("Hayat bazen zorlu bir mücadele gibi gelebilir. Yollarının ne kadar dik olduğunu, karşına çıkan engellerin ne kadar büyük olduğunu düşünerek, yorulup pes etmeye karar verebilirsin. Ancak hatırlaman gereken bir şey var: Her zorluk, yeni bir fırsat doğurur.")
    elif x == "çıkış":
        break        
    else:
        print("Adamım, lütfen... seçenekler var.")
