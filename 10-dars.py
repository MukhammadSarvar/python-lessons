"""

 10-dars 

TOPIC: TARMOQLANISH
    

Created on Tue Jul 30 17:16:13 2024

@author: MukhammadSarvar

"""

avtolar = ['bmw', 'audi', 'range rover','ferrari','bugatti']
for avto in avtolar:
    # avtolar ichidaagi har bir avto uchun 
    if avto == 'bmw': # < == >  tengmi degani
        # agar avto "bmw" ga teng bo'lsa
        print(avto.upper())
    else:#aks holda
        print(avto.title())

# qachonki if sharti TRUE qaytarsha u bajariladi, FALSE qaytarsa u bajarilmaydi



ism = input("Ismingizni kiriting\n>>>")
if ism.lower() != 'ali':
    # < != > teng emasmi?
    # bunda operator kiritilgan matnni kichik qilib aliga tenglab ko'radi
    print(f"Uzr,{ism.title()} biz Alini kutayabmiz!")
else:
    print("Salom,Ali")



javob = float(input("12x6 nechaga teng?\t>>>"))
if javob != 72:
    print("Javob xato!")

# kodning davomi bo'lmagani uchun dastur to'liq ishlamaydi


yosh = int(input("Yoshingiz nechada?\n>>>"))
if yosh >= 18:
    # katta yoki tengligini tekshiradi
    print("Xo'sh kelibsiz!")
else:
    print("Kirish mumkin emas!")



login = input("Yangi login kiriting:")
if len(login) <= 5 : 
    # len() loginni uzunligini hisoblaydi
    print("Login 5 ta belgidan ko'p bo'lishi shart!")



yil = int(input("Tug'ilgan yilingizni kiriting:\n"))
if 2024-yil < 18:# foydalanuvchining yoshini hisoblaymiz
    print(f"Sizning yoshingiz {2024-yil}da ekan!")
    print("Sizga kirish mumkin emas!")
else:
    print("Xo'sh kelibsiz")



nafaqa = int(input("Tug'ilgan yilingizni kiriting:\n"))
if 2024-nafaqa > 60: print("Siz nafaqa yoshida ekansiz!")
# qisqaroq qilib bir qatorga yozish ham mumkin

x,y = 30,45 # x=30, y=25
print("x>y") if x>y else print("x<y")
# if ning badani ifdan oldin keladi else ning badani  esa elsedan keyin keladi
# agar if else ni bir qatorga yozsak unda birinchi print() yoziladi va u if tegishli bo'ladi 
# oxirgi kiritilgan print() esa else ga tegishli bo'ladi


"""
dars vaqti:   21:02
ketgan vaqt:  56:19

"""