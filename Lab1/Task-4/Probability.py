print("Введите три вероятноcти для страшного оползня: для Никиты, Сережи и Насти.")
print("P.S.Ввероятность может принимать значения от 0 до 1")
Nicita=float(input("Никита: "))
Serezha=float(input("Сережа: "))
Nastya=float(input("Настя: "))
C = 14
D = 200
if ((Nicita > 1) or (Serezha > 1) or (Nastya > 1) or (Nicita < 0) or (Serezha < 0) or (Nastya < 0)):
        print("Ввероятность может принимать значения от 0 до 1!!!")
else:
        # Считаем вероятность страшного оползня для Никиты
        Answer = float((1 - (1 - Nicita)**(D/C))*(1 - Serezha**(D/C))*(1 - Nastya**(D/C)))
        # Округляем ответ
        Answer = round(Answer, 3)
        # Выводим ответ
        print("Вероятность того, что за 200 дней оползень произойдет только с Никитой: " + str(Answer) )

