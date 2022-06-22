while True:
    sicaklik = int(input("Bir Sıcaklık Giriniz : "))
    celsius = (sicaklik * 9) / 5 + 32
    fahrenheit = ((sicaklik - 32) * 5) / 9
    print("Sicaklık Biriminiz Nedir?"
        "\n1 = Celsius\n"
        "2 = Fahrenheit")
    sicaklikBirimi = str(input("Sıcaklığınızın Birimini yazınız : "))

    if sicaklikBirimi == "1":
        y = str(input("bu değeri fahrenheit'e çevirmek ister misiniz ? "))
        if y == "Evet":
            sicaklikBirimi = celsius
            print(sicaklikBirimi)
        elif y == "Hayır":
            print("Değeriniz Celsius.")
        else:
            print("Hatalı Bir İşlem oldu üzgünüz.")


    if sicaklikBirimi == "2":
        y = str(input("bu değeri celsius'e çevirmek ister misiniz ? "))
        if y == "Evet":
            sicaklikBirimi = fahrenheit
            print(sicaklikBirimi)
        elif y == "Hayır":
            print("Değeriniz Fahrenheit.")
        else:
            print("Hatalı Bir İşlem oldu üzgünüz.")

    deger = str(input("Çıkmak istiyor musunuz?\n"
                      "1-Evet\n"
                      "2-Hayır\n"
                      "Cevabınız : \n"))
    
    if deger == int(deger)==1:
        break
    elif deger == int(deger)==2:
        continue