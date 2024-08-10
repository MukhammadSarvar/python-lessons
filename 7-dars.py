
"""
 7-dars 

TOPIC: LIST 
    
Created on Mon Jul 29 13:04:02 2024

@author: MukhammadSarvar

"""

mevalar = ["olma", "anjir","O'RIK","shaftoli"]
# ro'yhat mevalar matndan tashkil topgan
narhlar = [12000,17000,5000,13000]
# narhlar ro'yhati sonlardan iborat
sonlar = ['bir','ikki',3,4,5]
#biz ro'yhatga ham sonlar va matnlarni aralash saqlashimiz mumkin 
ismlar = []# va shuningdek bo'sh ro'yhat ham yaratishimiz mumkin

# dasturlash tillarida sanash har doim 0 dan boshlanadi 
print("Birinchi meva:",mevalar[0])
#birinchi elementni chaqirish uchun 0 ni quyamiz sabab 0 dan boshlab salangani uchun 
print("Ikkinchi meva:", mevalar[1])# 1 bu ikkinchi elementi anglatadi
print("Uchinchi element:",mevalar[-2])
# biz ro'yhadagi elementga teskarisiga ham murojaat qilishimiz mumkin yani manfiy sanash orqali
print("To'rtinchi element:",mevalar[-1].upper())
print("Birinchi meva:",mevalar[-4].capitalize())
print("Ikkinchi meva:", mevalar[-3].title())
print("Uchinchi element:",mevalar[2].lower())


print(narhlar[1] + narhlar[3])
# agar ro'yhat sonlardsan iborat bo'lsa biz ular ustida arifmetik amallar bajarishimiz mumkin
print(narhlar[0] + 11000) 

    # Elementlarni o'zgartirish
mevalar[0] = 'banan'
# elemntni o'zgartirish uchun aynan uziga murojaat qilib uni boshqasiga tenglaymiz
print(mevalar)



    # .append()
# append() metodi ro'yhatga element qo'shish uchun ishlatiladi u har doim elementni  ro'yhatning oxiriga qo'shadi
mevalar.append('uzum')
print(mevalar)

    #insert()
# agar ro'yhatning boshiga yoki oxiriga element qo'shmoqchi bo'lsak unda insert() metodidan foydalanamuiz
mevalar.insert(0,'banan' )
#insertda birinchi kiritmoqchi bo'lgan elementimizni indexni kiritamiz keyin elementni
mevalar.insert(2, 'uzum')
print(mevalar)



cars = []
cars.append('rolls royes')
cars.append('range rover')
cars.append('K5')
cars.append('BMW')
print(cars)
# ro'yhatdagi malum bir elementni o'chirish uchun esa to'g'ridan to'g'ri indexiga murojat qilib o'chirish mumkin
del cars[2]
print(cars)
cars.insert(2,'k5')
print(cars)



  # .remove()
# agar ro'yhat ichida element ko'p bo'lsa va elementning tartib raqamini bilmasak unda <remove> da foydalanamiz
cars.remove("K5")
print(cars)

hayvonlar = ['it' ,'mushuk','qo\'y', 'echki','sigir','mushuk']
#print(hayvonlar)
hayvonlar.remove('mushuk')
#remove bu ro'yhatdagi faqat birinchi uchragan elementni o'chirib tashlaydi
hayvonlar.remove('mushuk') #agar ularni hammasini o'chish uchun esa qayta qayta takrorlash kerak bo'ladi
print(hayvonlar)



  # .pop()
# bu ro'yhatdagi elementni sug'urib oladi va boshqasiga joylaydi
bozorlik = ['yog\'', 'un','kartoshka',"go'sht",'sabzi']
mahsulot =bozorlik.pop(3)
# ro'yhatdan go'shtni sug'urib olamiz
print("Men " + mahsulot + "ni sotib oldim ")
print("Olinmagan mahsulotlar:" ,bozorlik)

mahsulot2 = bozorlik.pop()
# agar biz pop() metodidan foydalanganda hecha qanaqa index yozmasak unda u oxirgi elementni sug'urib oladi
print(mahsulot2)

"""
dars vaqti:   24:23
ketgan vaqt:  01:21:19

"""
