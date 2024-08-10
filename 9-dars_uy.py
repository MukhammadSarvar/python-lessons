"""

9-dars_uy

Created on Fri Aug  2 17:54:12 2024


"""

    #1
#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Ali',"Vali",'hasan','husan','john']
for ism in ismlar:
    print("Assalom alaykum,", ism.title())


    #2
#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")


    #3
#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)



    #4
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("Beshta eng yaxshi ko'rgan filimingiz?")
for kino in range(1,6):
    kinolar.append(input(f"{kino} yaxshi ko'rgan filmingizni kiriting:\n>>>"))
print(kinolar)




    #5
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
#va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_odam = int(input("Bugun nechta odam bilan ko'rishdingiz?\n>>>"))
odamlar =[]
for r in range(n_odam):
    odamlar.append(input(f"Bugun {r+1}-chi suhbat qilgan odamingiz kim edi:\n"))
print(odamlar)




"""
ketgan vaqt:  27:28

"""