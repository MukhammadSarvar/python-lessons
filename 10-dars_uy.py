"""

10-dars_uy 


Created on Fri Aug  2 16:47:11 2024


"""
     #1
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
#ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.capitalize())


    #2
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())



    #3
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa,
#"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
#Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
login = input("Loginingizni kiriting:\n>>>")
if login.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yhatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login.title()}!")


      #4
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son1 = float(input("Birinchi sonni kiriting:"))
son2 = float(input("Ikkinchi sonni kiriting:"))
if son1 == son2:
    print("Sonlar teng")



    #5
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son",
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son = float(input("Istalgan son kiriting:"))
print("Manfiy son") if son <0 else print("Musbat son")


     #6
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
#Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
f_son= float(input("Biror son kiriting:"))
print(f_son**(1/2)) if f_son > 0 else print("Musbat son kiriting!")


"""
ketgan vaqt:  20:53

"""