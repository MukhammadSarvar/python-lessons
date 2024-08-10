"""

5-dars_uy

Created on Fri Aug  2 03:48:03 2024


"""

      #1
#Quyidagi o'zgaruvchilarni yarating:
kucha = "Bog'bon"
mahalla = 'Sog\'bon'
tuman = "Bodomzor"
viloyat = "Samarqand"


    #2
#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
print(kucha,"ko'chasi,", mahalla,"mahallasi,",tuman, "tumani,", viloyat,"viloyati")    
    
   
    #3    
# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang
print("Iltimos quyidagi ma'lumotlarni kiriting:")
fkocha = input("Ko'changiz: ")
fmahalla = input("Mahallangiz: ")
ftuman = input("Tumaningiz: ")
fviloyat = input("Viloyatingiz: ")
print(fkocha + " ko'chasi,", fmahalla+" mahallasi,", ftuman+" tumani,", fviloyat+" viloyati")


      #4
#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print(fkocha + " ko'chasi,\n", fmahalla+" mahallasi,\n", ftuman+" tumani,\n", fviloyat+" viloyati")


      #5
#Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil =f"{kucha} ko'chasi, {mahalla} mahallasi, {tuman} tumani,{viloyat} viloyati "
print(manzil)

      #6
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print(fkocha.capitalize() + " ko'chasi,", fmahalla.upper()+" mahallasi,", ftuman.title()+" tumani,", 
      fviloyat.lower()+" viloyati")


"""
ketgan vaqt:  27:17

"""

      