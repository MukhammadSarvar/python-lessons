"""

 11-dars 

TOPIC: If-elif-else
    

Created on Sun Aug  4 02:23:56 2024

@author: MukhammadSarvar

"""

yosh = int(input("Yoshingiz nechada?"))
if yosh <= 4:
    print("Sizga kirish bepul")
elif yosh <= 12:
    print("Sizga kirish 5000 so\'m ")
elif yosh <= 18:
    print("Sizga kirish 10000 so'm ")
else:
    print("Sizga kiris 20000 so'm ")
#elif bu if va else ni birlashgani bo'lib biz ikkita emas bir nechta shart kiritganimizda ishlatamiz
# elifni xoxlagancha kiritish mumkin

# bu agar birinchi shart bajarilsa qolgan shart tekshirilmaydi



kun = input("Bugun kun niima?\n>>>")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    # or operaatori kiritilsa ikkalasidan biri to'g'ri bo'lsa ham  if bajariladi
    print("Bugun dam olish kuni!")
else:
    print("Bugun ish kuni!")
    
    
kun = input("Bugun kun niima?\n>>>")    
harorat = int(input("Bugun harorat nechchi?\n>>>"))
if kun.lower() == 'yakshanba' and harorat >= 30:
    # and operatori qullanganda ikkala shart ham to'g'ri bo'lishi kerak
    print("Cho'milgani ketdik!")
elif kun.capitalize() == "Yakshanba" and harorat < 30:
    # ikkila shart to'g'ri bo'lsagina bu shart bajariladi
    print("Uyda dam olamiz!")    
    
    
    
kun = input("Bugun kun niima?\n>>>")    
harorat = int(input("Bugun harorat nechchi?\n>>>"))
if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30:
    print("Cho'milgani ketdik!")
elif (kun.capitalize() == "Yakshanba" or kun.lower() == 'shanba') and harorat < 30:
    print("Uyda dam olamiz!")    



narh = 13000 # mijoz 13000 so'mga osh sotib oldi
choy = True # mijoy choy ham sotib oldi
salat = True # mijoz salat olmadi 

if choy and salat:
    # agar mijoz choy va salat sotib olgan bo'lsa 10000 qo'shamiz 
    narh = narh + 10000
elif choy or salat :
    # agar mijoz choy yoki salat sotib olgan bo'lsa 5000 qo'shamiz
    narh = narh + 5000
print(f"Jami narh {narh} so'm")



qiymat = 15000 
salet = False
non =1
k_choy = True
kompat = 0
shirinlik = True
if salet:
    print("Mijoz salat oldi.")
    qiymat= qiymat + 4000
if non:
    print("Mijoz non oldi.")
    qiymat= qiymat + 2000
if k_choy:
    print("Mijoz ko'k choy oldi.")
    qiymat = qiymat + 3000
if kompat:
    print("Mijoz kompat oldi.")
    qiymat = qiymat + 5000
if shirinlik:
    print("Mijoz shirinlik oldi.")
    qiymat= qiymat+ 7000
# bu yerda if lar bir qancha bo'lgani uchun birinchi shart bajariladimi yuqmi kiyingisiga utadi va uni tekshiradi
print(f"Jami narh {qiymat} so'm")



            # in 
# in yordamida ro'yhatni ichida bor yuqligini tekshirishimiz mumkin 
menu =['osh','qozankabob','somsa','shurva','manti','norin']
ovqat = input("Nima ovqat buyurasiz?\n>>>")
if ovqat.lower() in menu:
    print("Buyurtmangiz qabul qilindi!")
else:
    print("Kechirasiz bizda bunday ovqat mavjud emas!")
# Buning teskarisi yuqligini tekshirish uchun < NOT IN > dan foydalanamiz


menu =['osh','qozankabob','somsa','shurva','manti','norin']
buyurtmalar = ['osh','shashlik','norin','baliq']
if buyurtmalar: # ro'yhatni bush emasligini tekshiramiz
# agar ro'yhatda biror element bo'la bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yhat bush bo'lsa 
    print("Savatchangiz bo'sh.")


"""
dars vaqti:   25:56
ketgan vaqt:  01:25:45

"""






