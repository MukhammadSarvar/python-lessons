"""

 9-dars 

TOPIC: FOR LOOP
    
Created on Tue Jul 30 03:43:31 2024

@author: MukhammadSarvar

"""

mehmonlar = ['ali','vali','hasan','husan','bek']
for mehmon in mehmonlar :
    # for bu yerda ma'lum bir kodni qayta-qayta takrorlaydi   
    print("Salom",mehmon)
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 2-avgusdagi nahorgi oshga taklif qilamiz!")
    print("Hurmat bilan, Palonchiyevlar oilasi\n")
    
    
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son}ning kvadrati {son**2}ga teng.")
    
sonlar =list(range(11))    
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)


dustlar =[]
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    
 # n bu yerda 0 dan 4 gacha bo'lgan raqamlarda tartiblanadi
    dustlar.append(input(f"{n+1} do'stingizning ismini kiriting.\n"))
print(dustlar)
print(dustlar[1])
# # yoki
# for x in range(1,6):
#     dustlar.append(input(f"{n} kiriting"))



"""
dars vaqti:   13:07
ketgan vaqt:  40:00

"""