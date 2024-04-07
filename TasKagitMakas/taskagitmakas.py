import random
print("Taş Kağıt Makas ?")
pcskor=0
kullaniciskor=0
list1=["Taş","Kağıt","Makas"]
while True:
    if pcskor==3 or kullaniciskor==3:
        break
    kullanici=input("Hamle Seçin  = ")
    bot=(random.choice(list1))
    print("Bilgisayar Seçimi = ",bot)  
    
    if kullanici=="Taş" and bot=="Taş":
        print("Berabere")
    
    elif kullanici=="Taş"and bot=="Kağıt":
        print("Bilgisayar Kazandı Puan +1 Arttırıldı")
        pcskor=pcskor+1
        print("Bilgisayar Puanı :",pcskor,"Kullanıcı Puanı :",kullaniciskor)
        
    elif kullanici=="Taş" and bot=="Makas":
        print("Kazandınız Puanınıza +1 Arttırıldı ")
        kullaniciskor+=1
        print("Bilgisayar Puanı :",pcskor,"Kullanıcı Puanı :",kullaniciskor)
    
    elif kullanici=="Kağıt" and bot=="Taş":
        print("Kazandınız Puanınıza +1 Arttırıldı ")
        kullaniciskor+=1
        print("Bilgisayar Puanı :",pcskor,"Kullanıcı Puanı :",kullaniciskor)

    elif kullanici=="Kağıt" and bot=="Kağıt":
        print("Berabere")

    elif kullanici=="Kağıt" and bot=="Makas":
        print("Kaybettiniz ")
        pcskor=pcskor+1
        print("Bilgisayar Puanı :",pcskor,"Kullanıcı Puanı :",kullaniciskor)
    
    elif kullanici=="Makas" and bot=="Taş":
        print("Kaybettiniz ")
        pcskor=pcskor+1
        print("Bilgisayar Puanı :",pcskor,"Kullanıcı Puanı :",kullaniciskor)

    elif kullanici=="Makas" and bot=="Makas":
        print("Berabere")
    
    elif kullanici=="Makas" and bot=="Kağıt":
        print("Kazandınız Puanınıza +1 Arttırıldı ")
        kullaniciskor=kullaniciskor+1
        print("Bilgisayar Puanı :",pcskor,"Kullanıcı Puanı :",kullaniciskor)
    



