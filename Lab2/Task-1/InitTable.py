from openpyxl import Workbook
import random

random.seed()

def initTable():

	wb = Workbook()
	ws = wb.active

	upper_limit = 20
	lower_limit = -20

	coords = set()

	ws['A1'] = 'x'
	ws['A2'] = 'y'

	for col in range(2, 17):
		unique_coords = False
		while not unique_coords:
			x_y = (random.uniform(lower_limit, upper_limit), random.uniform(lower_limit, upper_limit))
			if x_y not in coords:
				unique_coords = True
				coords.add(x_y)
				ws.cell(column=col, row=1, value=x_y[0])
				ws.cell(column=col, row=2, value=x_y[1])


	wb.save("Data.xlsx")



if __name__ == '__main__':
	initTable()