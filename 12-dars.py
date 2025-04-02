#print ("Hello World!")
#print("Hello World!")
#print("Hello World!")

#print("O'ngacha sanaymiz")
#for n in range(10):
#    print(n+1)
    
son = 50
if son>=0:
    print("Musbat son")
else:
    print("Manfiy son")
    
#son = input("Istalgan son kiriting: ")
#son=int(son)
#print(f"{son} ning kvadrati {son**2} ga teng")

#mevalar = ['olma','uzum','nok','anor','anjir']
#for meva in mevalar:
#    print(meva)
 
#son = float(input("Istalgan son kiriting: "))
#if son>=0:
#    print("Musbat son")
#else:
#    print("Manfiy son")   

#mevalar = ['olma','anor','uzum']
#print(mevalar[2])

#radius = 5
#pi = 3.14
#aylana_yuzi = pi*radius**2
#print(aylana_yuzi)

#son = float(input("Istalgan son kiriting: "))
#ildiz = son**(1/2)
#print(f"{son} ning ildizi {ildiz} ga teng")

#mevalar = ['olma','uzum','nok','anor','anjir']
#for meva in mevalar:
#    print(meva)
#print("Dastur tugadi")

#vAZIFA

#son = float(input("Juft son kiriting: "))
#if son%2!=0 :
#    print("Bu son juft emas.")
#else:
#    print("Rahmat!")


#yosh = int(input("Yoshingiz nechida?"))

#if yosh<=4 or yosh>=60:
#    narh1 = 0
#    print(f"Chiptangiz {narh1} so'm")
#elif yosh < 18:
#    narh2 = 10000
#    print(f"Chiptangiz {narh2} so'm")
#else:
#    narh3 = 20000
#    print(f"Chiptangiz {narh3} so'm")

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f'{x}<{y}')
#else:
#    print(f"{x}>{y}")
    
#mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat=mahsulot=[]

#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#if savat:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            print(f"Do'konimizda {mahsulot} bor")
#        else:
#            print(f"Do'konimizda {mahsulot} yo'q")
#else: 
#    print("Savatingiz bo'sh")            


mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)


if  mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor qidirib o'tirmang")
   