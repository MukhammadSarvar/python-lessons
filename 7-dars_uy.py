"""

7-dars_uy

Created on Fri Aug  2 04:44:37 2024


"""
         #1
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ["Bekzod","Dilshod","James" ]

        #2
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
print("Salom", ismlar[0],"!\n",
      ismlar[1], ", bugun darsga kelasanmi?\n"
      "Ishlaring yaxshimi,", ismlar[2])


       #3
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar =[12,34,56,67.8,23,-90,-32,-4,0,3.1,234_890_756_491]
print(sonlar)

      #4
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring
sonlar[0] = 45
sonlar[1]= sonlar[1] + sonlar[-1]
sonlar[3] = sonlar[3] + 45
del sonlar[8] 
sonlar[9] = sonlar[9] - sonlar[7]
print(sonlar)


        #5
#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan 
#tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar =["Alisher Navoiy","AL-Xorazmiy","Jaloliddin Rumiy"]
t_shaxslar1 = t_shaxslar.pop(2)
z_shaxslar =["Stive Jobs", "Bell Gates","Jeff Bezos"]
z_shaxslar1 = z_shaxslar.pop(1)



       #6
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print("Men tarixiy shaxslardan " + t_shaxslar1 + " bilan, zamonaviylaridan esa " + z_shaxslar1+ " bilan suhbat qilishni hohlardim." )



      #7
#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends =[]
friends.append('Dilshod')
friends.append("Botir")
friends.append("Zokir")
friends.append("Abulkarim")
friends.append('John')
#print(friends)




        #8
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove('Dilshod')
friends.remove('John')
print(friends)



       #9
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Jahongir')
friends.insert(0, 'Bobur')
friends.insert(2, 'Bekzod')
print(friends)


      #10
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, 
#mehmonlar ro'yxatiga qo'shing.

mehmonlar =[]
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
print("Mehmonga kelganlar:", mehmonlar)



"""
ketgan vaqt:  38:40

"""
