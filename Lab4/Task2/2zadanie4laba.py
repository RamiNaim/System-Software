


# Вывод матрицы
def out (matrix):
	if matrix != None:
		for i in range (0, rows(matrix)):
			print(matrix[i])
	return " "
def rows(matrix):
	rows = len(matrix)
	return rows


# Вывод числитля и знаменателя передаточной функции
def function(A, B, C):	
	koef = []
	k1 = -A[0][0]*A[1][1]*A[2][2]+A[0][0]*A[2][1]*A[1][2]+A[1][0]*A[2][2]*A[0][1]-A[1][0]*A[0][2]*A[2][1]-A[2][0]*A[0][1]*A[1][2]+A[0][2]*A[1][1]*A[2][0]
	koef.append(k1)
	k2 = A[1][1]*A[2][2]-A[2][1]*A[1][2]+A[0][0]*A[2][2]+A[0][0]*A[1][1]-A[1][0]*A[0][1]-A[2][0]*A[0][2]
	koef.append(k2)
	k3 = -A[0][0]-A[1][1]-A[2][2]
	koef.append(k3)
	koef.append(1)
	koef2 = []
	k12 = ( B[0][0]*C[0][0]*(A[1][2]*A[2][1]-A[1][1]*A[2][2]) + B[0][0]*C[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][1]) + B[0][0]*C[0][2]*(A[1][1]*A[2][0]-A[1][0]*A[2][1])
                + B[1][0]*C[0][0]*(A[0][1]*A[2][2]-A[0][1]*A[2][2]) + B[1][0]*C[0][1]*(A[0][2]*A[2][0]-A[2][2]*A[0][0]) + B[2][0]*C[0][2]*(A[0][0]*A[2][1]-A[0][1]*A[2][0])
                + B[2][0]*C[0][0]*(A[0][2]*A[2][2]-A[0][1]*A[1][2]) + B[2][0]*C[0][1]*(A[0][0]*A[1][2]-A[0][2]*A[1][0]) + B[2][0]*C[0][2]*(A[0][1]*A[1][0]-A[0][0]*A[1][1]) )
	koef2.append(k12)
	k22 = ( B[0][0]*C[0][0]*(A[1][1]+A[2][2]) - B[0][0]*C[0][1]*A[1][0] - B[0][0]*C[0][2]*A[2][0] - B[1][0]*C[0][0]*A[0][1] + B[1][0]*C[0][1]*(A[0][0]+A[2][2])
                - B[1][0]*C[0][2]*A[2][1] - B[2][0]*C[0][0]*A[0][2] - B[2][0]*C[0][1]*A[1][2] + B[2][0]*C[0][2]*(A[0][0]+A[1][1]) )
	koef2.append(k22)
	k32 =((-B[0][0]*C[0][0])+(-B[1][0]*C[0][1])+(-B[2][0]*C[0][2]))
	koef2.append(k32)
	
	signs = []
	sign = "+" if koef2[0]>0 else "-"
	signs.append( sign )
	sign = "+" if koef2[1]>0 else "-"
	signs.append( sign )
	sign = "" if koef2[2]>0 else "-"
	signs.append( sign )
	
	

	print ("Числитель передаточной функции:")
	print (signs[2] + str(abs(koef2[2])) + 's^2' + signs[1] + str(abs(koef2[1]))+'s' + signs[0] + str(abs(koef2[0])))
	print('\n')

	signs = []
	sign = "+" if koef[0]>0 else "-"
	signs.append( sign )
	sign = "+" if koef[1]>0 else "-"
	signs.append( sign )
	sign = "+" if koef[2]>0 else "-"
	signs.append( sign )

	print ("Знаменатель передаточной функции:")
	print ('s^3' + signs[0] + str(abs(koef[2]))+'s^2' + signs[1] +str(abs(koef[1]))+'s' + signs[0] +str(abs(koef[0])))
	print('\n')
		

if __name__ == '__main__':
	A = [[0,1,0],[0,0,1],[-1,-1,-3]]
	B = [[9],[-1],[5]]
	C = [[1,6,5]]
	print("Матрица А:")
	print(out(A))
	print('\n')
	print("Матрица B:")
	print(out(B))
	print('\n')
	print("Матрица C:")
	print(out(C))
	print('\n')	
	function(A, B, C)

