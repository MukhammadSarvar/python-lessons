"""

   6-dars 

TOPIC:  SONLAR
    
Created on Mon Jul 29 09:56:25 2024

@author: MukhammadSarvar

"""
a = 20 # <int> bu butun son 
b = 5.9# <float> bu o'nlik son
temp = 36.6
print(type(a))
#type bu o'zgaruvchini turini aniqlaydi 
aholi_soni = 7_789_456_846
print("Aholi soni:", aholi_soni)
# agar sonlar judayam uzun bo'lsa uni pastki chiziq bilan yozish mumkin. Bu pythonda muammo emas


x,y,z = 6, 7.8, -34
#biz pythonda bir nechta o'zgaruvchiga bir qatorda qiymat berishimiz mumkin

c= a * b
# agar biz bajargan amalda bitta son o'nlik bo'lsa natija ham o'nlik bo'ladi



#agar o'zgaruvchi katta harflarda yozilsa bu dastur davomida o'zgarmas constanta bo'lib saqlanadi
radius = 10
PI = 3.14159
diametr = 2*radius
print("Aylana uzunligi=",PI*diametr) 



ism = "Sarvar"
yosh = 21
xabar = ism +  " " + str(yosh) + " yoshda"
print(xabar)
# str va int birlashtirib bo'lmaydi
# buning uchun esa yoshni uzini emas natijani o'zgartirib olamiz 



t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2024 - t_yil
print("siz ", yosh ," yoshda ekansiz.")
# input foydalanuvchidan kiritilgan har qanday ma'lumotni string ko'rinishida saqlaydi



a = int("12")# int orqali matndan butun songa utib oldik 
b = float("12") # float orqali esa matnda o'nlik songa utib oldik
temp = str(36.6) # bu yerda esa o'nlik sondan matnda utib oldik
# faqatgina o'nlik sondan butun songa utib bo'lmaydi xolos 

"""
dars vaqti:   21:49
ketgan vaqt:  54:19

"""
