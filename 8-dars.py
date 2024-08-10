"""

 8-dars 

TOPIC: LISTS
    
Created on Mon Jul 29 16:54:02 2024

@author: MukhammadSarvar

"""
    # Tartiblash
cars = ['bmw','audi','mercedes benz','range rover', 'toyota','ferrari']
cars.sort()
# sort() bu ro'yhatni alifbo tartibida shakllantiradi 
print(cars)
# bu yerda sort metodi agar ro'yhatda katta harf va
# kichik harfda boshlangan so'zlar bo'lsa birinchi u 
#katta harf bilan boshlangani oladi

cars.sort(reverse=True)
#reverse=True bu yerda teskari tartiblash uchun ishlatiladi
print(cars)

    #sorted() 
print(sorted(cars))
# bu ro'yhatni o'zgartirmasdan tahlangan holda consolga chiqaradi
print(sorted(cars,reverse=True))

sonlar =[12,34,75,89,9,5,-3,-78,17,91,78.9,33.3]
print(sorted(sonlar))
# bunda sonlar ham kichigidan kattasiga qarab taxlanadi
sonlar.sort(reverse=True)
print(sonlar)

cars.reverse()
#reverse() yordamida ro'yhatni teskari qilib quyish ham mumkin
print(cars)


      #len
print(len(cars))
# len bu ro'yhat uzunligini aniqlaydi
print(len(sonlar))



    #range()
# range bu malum oraliqdagi sonlarni shaklllantiradi
juft_sonlar = list(range(2,101,2))
# range funksiyasi boshlangan raqamni uz ichiga oladi ammo oxirgisini olmaydi
toq_sonlar = list(range(1,100,2))# bu yerda 100 kirmaydi, 100gacha bo'lgani kiradi
# boshlanish va tugash nuqtalarini quygandan keyin yozilgan raqam shuncha sakrab utishini anglatadi 
print("Yuzgacha bo'lgan juft sonlar:",juft_sonlar)
print("Yuzgacha bo'lgan toq sonlar:",toq_sonlar )

    # min() max() sum()
narhlar =[12000,31000,9800,23000,4500,5600,13000]
arzon = min(narhlar) 
# min bu yerdagi eng kichigini oladi
qimmat = max(narhlar)
#max bu yerda eng kattasini oladi
jami = sum(narhlar)
# sum jami yig'indisini hisoblaydi
print("Eng arzon narx:",arzon,".Eng qimmat narx:",qimmat,".Umumiy narz:",jami)


      # RO'YHATNI KESISH
cars = ['bmw','audi','mercedes benz','range rover', 'toyota','ferrari']
my_cars = cars[0:3] # 0-indexdan boshlab 3 ta element ajratib oladi
print(my_cars)
print(cars[2:5]) #2-indexdan boshlab 5 gacha qabul qiladi
print(cars[:4]) 
# agar birinchi elementni yozmasak uz-uzidan u 0 dan boshlab hisoblaydi
print(cars[3:])
 # agar birinchi elementni yozib oxirgisini yozmasak u holda oxirigacha hisoblaydi



    # ro'yhatdan nusxa olish
my_cars = cars
# bu yerda muammo my carsga qushsak ham carsga qushilib qoladi
my_cars.remove('audi')
my_cars.append('malibu')
my_cars.insert(3, 'bugatti')

print(my_cars)
# bu holda nusxa olinmaydi nusxa olish uchun esa 
my_cars1 = cars[:]
#bu carsdan hammasini  nusxalab oladi
# nusxa olish uchun boshlang'ich va oxirgi elementlarni kiritmaymiz
# nusxa olish uchun kesib olamiz
my_cars1.remove('toyota')
my_cars1.append('gentra')
my_cars1.insert(1, 'bugatti')
print(my_cars1)



    #TUPLES(o'zgarmas ro'yhat)
toys = ('snake', 'teddy','bus','car','train','bear')
print(toys[0])
print(toys[3])
print(toys[:4])
print(toys[2:])

# agar tupleni o'zgartirish kerak bo'lib qolsa 
toys= list(toys)
print(type(toys))
toys.append('lezard')
toys.remove('bus')
print(toys)
toys =tuple(toys)



"""
dars vaqti:   26:57
ketgan vaqt:  01:32:31

"""
