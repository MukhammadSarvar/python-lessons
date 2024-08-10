"""

8-dars_uy

Created on Fri Aug  2 15:28:53 2024

"""

       #1
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["Uzbekiston","Qozog'iston","Tojikiston","Turkmaniston","Qirg'isiston"]
print(davlatlar)


     #2
#Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))


      #3
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))


    #4
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar,reverse=True))



      #5
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(davlatlar)


    #6
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)


     #7
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)



     #8
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1201))
print(sonlar)


     #9
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar))


      #10
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
qiymat = max(sonlar) - min(sonlar)
print(qiymat)



     #11
# Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar))



    #12
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[500:520])
print(sonlar[-20:])



      #13
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = []
taomlar.append('manti')
taomlar.append('lag\'mon')
taomlar.append('palov')
taomlar.append('staek')
taomlar.append('shashlik')
print(taomlar)



     #14
#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
print(nonushta)



     #15
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('palov')
nonushta.remove('manti')
nonushta.remove('staek')
nonushta.append('katoshka qovurma')
nonushta.append('norin')
print(nonushta)


    #16
#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)


    #17
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta =tuple(nonushta)
print(type(nonushta))


"""
ketgan vaqt:  41:00

"""