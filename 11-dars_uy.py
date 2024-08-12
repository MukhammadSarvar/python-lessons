"""

 11-dars_uy
    
Created on Mon Aug  5 01:33:56 2024


"""
    #1
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", 
#agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son = float(input("Juft son kiriting:\n>>>"))
if son%2: # bu agar son qoldig'i 0 bo'lmasa shart bajariladi
    print("Bu juft son emas!")
else:
    print("Rahmat!")


    #2
#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

    #Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
    #Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
    #Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = int(input("Yoshingizni kiriting:\n>>>"))
if yosh <= 4 or yosh >= 60:
    print("Sizga kirish bepul!")
elif yosh <= 18:
    print("Sizga kirish 10000 so'm!")
elif yosh >=18:
    print("Sizga kirish 20000 so'm!")



    #3
#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
son1 = float(input("Birinchi sonni kiriting:\t"))
son2 = float(input("Ikkinchi sonni kiritingh:\t"))
if son1==son2 :
    print("Sonlar teng!")
elif son1 > son2:
    print("Birinchi son ikkinchisidan katta!")
elif son1 < son2:
    print("Birinchi son ikkinchisidan kichik!")



    #4
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
  # Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
  # Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
  #"Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar = ['olma','shakar',"go'sht",'kartoshka' ,'un','guruch','uzum','sabzi','tuxum','pepsi']
savat =[]
for f in range(1,6):
    savat.append(input(f"{f}-chi mahsulotni kiriting:"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor.")
    else:
        print(f"Do'konimizda {mahsulot} yo'q.")




    #5
#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga,
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
#"Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
mahsulotlar = ['olma','shakar',"go'sht",'kartoshka' ,'un','guruch','uzum','sabzi','tuxum','pepsi']
savat =[]
for f in range(1,6):
    savat.append(input(f"{f}-chi mahsulotni kiriting:"))
bor_mahsulotlar =[]
mavjud_emas =[]
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas: # bo'sh yoki bo'sh emasligini tekshiramiz
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan hamma mahsulot do'konimizda bor!")



    #6
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
  #Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan
  # ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, 
  #"Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
foydalanuvchilar = ["tinch_quying",'eron_emmi',"nurzafarovich",'mukhammad_sarvar','oddiy_bola']
login= input("Yangi login kiriting:\n>>>")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")


    #7
#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha 
# bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
b_son = int(input("Butun son kiriting:\t"))
for n in range(2,11):
    if not (b_son % n ):
        print(f"{b_son} soni {n} ga qoldiqsiz bo'linadi!")

"""
ketgan vaqt:  01:04:44


5:7 

"""
