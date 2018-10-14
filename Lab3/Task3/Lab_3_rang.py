def rows(matrix):
	rows = len(matrix)
	return rows

def columns(matrix):
	columns = len(matrix[0])
	return columns

def out (matrix):
	if matrix != None:
		for i in range (0, rows(matrix)):
			print(matrix[i])
	return " "

def swap(matrix,i):
	k = 0
	if i == columns(matrix) or i == rows(matrix):
		pass
	else:
		for step in range (columns(matrix)-i):
			if matrix[i][i] == 0:
				matrix[i],matrix[i+step] = matrix[i+step],matrix[i]
			else: k = 1
	return matrix, k

def  check(matrix):
	list=[]
	for i in range (0,rows(matrix)):
		flag = 0
		for j in range(0, columns(matrix)):
			if matrix[i][j] != 0 : flag =1
		if flag ==0:
			list.append(i)
	step = 0
	for i in list:
		del matrix[i-step]
		step += 1
	list = [] 
	for j in range(0,len(matrix[0])):
		flag = 0
		for i in range (0, rows(matrix)):
			if matrix [i] [j] != 0 : flag = 1
		if flag == 0:
			list.append(j)
	step = 0
	for j in list:
		for i in range(0,rows(matrix)):
			del matrix[i][j-step]
		step += 1
	return matrix

def mult(matrix1,matrix2):
	i=0
	j=0
	k=0
	resultLine = 0
	if rows(matrix2) == columns(matrix1):
		result = []
		for i in range(rows(matrix1)):
			line=[]
			for j in range (len(matrix2[i])):
				for k in range(columns(matrix1)):
					resultLine += matrix1[i][k] * matrix2[k][j]
				line.append(resultLine)
				resultLine = 0
			result.append(line)
		else:
			return result
	else:
		return "Multiplication is impossible."

def power(matrix,power):
	i=0
	j=0
	k=0
	p=1
	resultPower=0
	if rows(matrix) == columns(matrix):
		matrixInPower = []
		while p < power:
			p+=1
			for i in range (rows(matrix)):
				line = []
				for j in range(columns(matrix)):
					for k in range (rows(matrix[i])):
						resultPower += matrix [i][k]*matrix [k][j]
					line.append(resultPower)
					resultPower=0
				matrixInPower.append(line)
		else:
			return matrixInPower
	else:
		return 'Matrix shoud be square'



def rang(matrix,n):
	ch_matr = check(matrix)
	f_matr, k = swap(ch_matr, n)
	minim = rows(f_matr) if (rows(f_matr)) <= columns (f_matr) else columns(f_matr)
	global r
	r = rows(matrix)
	N = n
	if (n < minim-1) or k != 0:
		for i in range(n+1, rows(f_matr)):
			kek = -f_matr[i][n]/f_matr[n][n]
			for j in range(n, columns(f_matr)):
				f_matr[i][j] = kek* f_matr[n][j]+f_matr[i][j]
		return rang(f_matr, n+1)
	else:
		return r

def observabilityMatrix(matrix1,matrix2):
	n = len(matrix2)*len(matrix2[0])
	result = [0]*n
	for i in range (n):
		result[i] = [0]* len(matrix2[0])
	result[0]= matrix2
	i=0 
	while i < (len(matrix2[0])-1):
		i += 1
		result[i]=mult(matrix2,matrix1)
		matrix1 = power(matrix1,i+1)
	result1 = [0]*n
	for i in range(n):
		result1[i] = []
	i = 0
	for j in range(len(matrix2[0])):
		for k in range(len(result[0])):
			result1[i] = result[j][k]
			i +=1
	return result1


def checkObservability(matrix1,matrix2):
	rangMatrix = rang(observabilityMatrix(matrix1,matrix2),0)
	n = columns(matrix2)
	if n == rangMatrix:
		return "The matrix is observable."
	else:
		return "The matrix is not observable."

def controllabilityMatrix(matrix1,matrix2):
	n = len(matrix2)*len(matrix2[0])
	result = [0]*n
	for i in range (n):
		result[i] = [0] * len(matrix2)
	result[0] = matrix2
	i=0
	while i < (len(matrix2)-1):
		i += 1
		result[i] = mult(matrix1,matrix2)
		matrix1 = power(matrix1,i+1)
	result1= [0] * len(matrix2)
	for i in range(len(matrix2)):
		result1[i] = []
	for i in range(len(matrix2)):
		for j in range (len(matrix2)):
			result1[i] = result1[i] + result[j][i]
	return result1

def checkControllability(matrix1,matrix2):
	rangMatrix = rang(controllabilityMatrix(matrix1,matrix2),0)
	n = rows(matrix2)
	if n == rangMatrix:
		return "The matrix is controllable."
	else:
		return "The matrix is not controllable."



import time
A = [[7,2,3],[0,5,6],[7,8,9]]
B = [[1],[2],[3]]
C = [[1,7,3]]
startTime = time.time()
print "ControllabilityMatrix:"
print out(controllabilityMatrix(A,B))
print "Observability natrix:"
print out(observabilityMatrix(A,C))
print (checkControllability(A,B))
print (checkObservability(A,B))
print("The rank of the matrix A is:")
print(rang(A,0))
endTime = time.time()
time = endTime - startTime
print "Time"
print time



