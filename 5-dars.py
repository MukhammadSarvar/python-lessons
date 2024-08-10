"""
   5-dars 

TOPIC:   STRING (matn)

Created on Sun Jul 28 17:18:30 2024

@author: MukhammadSarvar
"""
ism = "Sarvarbeek"

shahar = "koson"
viloyat = "qashqadaryo"
# o'zgaruvchining nomi lotin bo'lishi shart ,lekin o'zgaruvchini xoxlaganday yozish mumkin

matn = "Men yangi 📱 oldim "
print(matn)



  # string ustida amallar 
ism = "Bek"
print("My name is " + ism )

ism = "Ahmat"
familiya = "Qozonchi"
print(ism + familiya)
# bu yerda ism va familiya qo'shilib qoldi buni oldini olish uchun esa 
print(ism + ' ' + familiya)# bo'sh joy qoldiramiz 



   # f-string 
ism = "Ahmat"
sharif = "Lutfiy Qozonchi"
ism_sharif = f"{ism} {sharif}"
print(ism_sharif)
#f-string yordamida biz yangi o'zgaruvchiga matn yuklaymiz 
print(f"Mening ismim {ism}")

ism = "James"
familiya = "Bond"
print(f"Salom mening ismim {familiya}. {ism} {familiya}")
#f-string yordamida bir nechta matnlarni birlashtirishimiz mumkin 



    # maxsus belgilar 
print("Hello world!")
print("Hello \tworld!")# <\t> matn orasida katta bo'shliq qoldiradi
print("Hello \nworld!") #< \n > matnni yangi qatordan boshlatadi



  # string metodlar 
#metodlarni chaqirish uchun so'z nuqta va metod 
ism = "James"
familiya = "Bond"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper()) 
#.upper() hamma harflarni katta qilib beradi
# bu metodni qo'llaganimizda bizni o'zgaruvchini ichidagi qiymat o'zgarmaydi faqat undan olingan qiymat o'zgaradi
#agar o'zgaruvchini katta qiymatda saqlamoqchi bo'lsak
ism_sharif = ism_sharif.upper() # qilib qaytadan qiymat beramiz
print(ism_sharif.capitalize())
# bu matndagi faqat birinchi harfni katta qiladi
print(ism_sharif.lower())
# bu matndagi hamma harflarni kichkina qilib beradi
print(ism_sharif.title())
# bu matn ichidagi har bir so'zni birinchi harflarni katta qilib berdi

meva = "    olma    "
print("Men " + meva.lstrip() +"yaxshi ko'raman")
#.lstrip() bu chap tarfdagi bo'sh joyni olib tashlaydi
print("Men " + meva.rstrip() +" yaxshi ko'raman")
#.rstrip() bu o'ng tarafdagi bo'sh joyni olib tashlaydi 
print("Men " + meva.strip() +" yaxshi ko'raman")
#.strip esa ikki tarfdagi bo'shliqni olib tashlaydi 



   #INPUT
#input bu foydalanuvchidan ma'lumot olishdan iborat
ism = input("Ismingiz nima?\n")
print("Assalom alaykum, " + ism.capitalize())
# inputni qullash uchun avval o'zgaruvchi yaratib keyin unga yuklash kerak

"""
dars vaqti:   18:55
ketgan vaqt:  01:19:30

"""
