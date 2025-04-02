# B.R.R
# #1)
# son=1
# while son<5:
#     print(son,end='')
#     son=son+1

#2)
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="istalgan sonni kiriting"
# savol += (" to'xtatish uchun exit deb yozing: ")
# qiymat=''
# while qiymat != 'exit':             #while---toki degani
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi')

#3) ishora
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="istalgan sonni kiriting"
# savol += (" to'xtatish uchun exit deb yozing: ")
# ishora = True
# while ishora:             #while---toki degani
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')

#4) Break
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="istalgan sonni kiriting"
# savol += (" to'xtatish uchun exit deb yozing: ")
#
# while True:   #abadiy sikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')

#5) Break/continue
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         break
#     print(f"{son} ning kvadrati {son**2}")

#6) Continue
# son = 0
# while son <10:
#     son +=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

#7) infinite loop
# son = 0
# while son < 10:
#     son +=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


# Uyga vazifa

#1)
# savol = "Yaxshi ko'rgan kitobingizni nomini yozing"
# savol+= ( " ro'yxat tugasa stop so'zini yozing: ")
# qiymat = ''
# input(savol) == qiymat
# while qiymat != stop:
#         input(savol) != qiymat
#         if qiymat != 'stop':
#             break
# print("Dastur tugadi")


# 2)
# savol = "Yoshingizni yozing: "
# savol += "('exit' yoki 'quit' deb yozsangiz dasturdan chiqib ketasiz): "
#
# while True:
#     qiymat = input(savol)
#
#     if qiymat.lower() in ['exit', 'quit']:
#         print("Dastur tugadi.")
#         break
#
#     try:
#         yosh = int(qiymat)
#
#         if yosh < 7:
#             print("Sizga bilet narxi 2000 so'm")
#         elif 7 <= yosh < 18:
#             print("Sizga bilet narxi 3000 so'm")
#         elif 18 <= yosh < 65:
#             print("Sizga bilet narxi 10000 so'm")
#         else:
#             print("Sizga bilet tekin")
#
#     except ValueError:
#         print("Iltimos, yoshingizni raqamda kiriting.")

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else:
#         narh = 0
#
#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")




#3)
# savol= "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat sonni kiriting"
# savol += "(dasturlashni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = input(savol)
#     if qiymat.lower()=="exit":
#         print("Dastur tugadi")
#         break
#     try:
#         son=float(qiymat)
#         if son<0:
#             print("Iltimos musbat son kiriting.")
#             continue
#
#             ildiz = float(qiymat)**(0.5)
#
#         print(f"{son} ning ildizi {ildiz} ga teng")

savol = "Yaxshi ko'rgan kitobizni kiriting"
savol+= ("chiqish uchun 'exit' deb yozing: ")
while True:
     qiymat = input(savol)
     if qiymat == 'exit':
        break
     print("Dastur tugadi")



























