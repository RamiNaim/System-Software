print("Введите три вероятноcти для страшного оползня: для Никиты, Сережи и Насти.")
print("P.S.Ввероятность может принимать значения от 0 до 1")
Nicita=float(input())
Serezha=float(input())
Nastya=float(input())
C = 14
D = 200
if ((Nicita > 1) or (Serezha > 1) or (Nastya > 1)):
        print("Ввероятность может принимать значения от 0 до 1!!!")
else:
        Answer = float(Nicita*D/(C*3))/((Nicita + Serezha + Nastya)*(D/(C*3)))
        Answer = round(Answer, 3)
        print(Answer)

