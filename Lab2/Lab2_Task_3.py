from openpyxl import Workbook
import random

random.seed()

def initTable():
	wb = Workbook()
	ws = wb.active
	for i in range(1,16):
		for j in range(1,16):
			val = random.uniform(1,30)
			ws.cell(column=j, row=i, value=val)
	wb.save("C:\Users\Полина\Desktop\python\Data2.xlsx")

if __name__ == '__main__':
	initTable()

