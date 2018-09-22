from Lab2_Task_2 import *









if __name__ == '__main__':
	wb = Workbook()
	ws = wb.active
	initTable(wb, ws)
	print("Введите способ, которым хотите восстановить данные:")
	print("1. Винзорирование")
	print("2. Линеаризация")
	print("3. Корреляционное восстановление")
	users_pick = int( input() )
	if users_pick == 1:
		vinz(wb, ws)
	elif users_pick == 2:
		linapr(wb, ws)
	elif users_pick == 3:
		cor(wb, ws)