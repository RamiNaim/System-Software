def observabilityMatrix(matrix1,matrix2):
	size = np.shape(matrix2)
	n =size[0]*size[1]
	result = [0]*n
	for i in range (n):
		result[i] = [0]* size[1]
	result[0]= matrix2
	i=0 
	while i < (size[1]-1):
		i += 1
		result[i]=np.dot(matrix2,matrix1)
		matrix1 = np.linalg.matrix_power(matrix1, i+1)
	result1 = [0]*n
	for i in range(n):
		result1[i] = []
	i = 0
	for j in range(size[1]):
		for k in range(len(result[0])):
			result1[i] =result[j][k]
			i +=1
	resultend = np.array ([result1[0], result1[1],result1[2]])
	return resultend


def checkObservability(matrix1,matrix2):
	rangMatrix = np.linalg.matrix_rank(observabilityMatrix(matrix1,matrix2))
	size = np.shape(matrix2)
	n =size[1]
	if n == rangMatrix:
		return "The matrix is observable."
	else:
		return "The matrix is not observable."


def controllabilityMatrix(matrix1,matrix2):
	size = np.shape(matrix2)
	n =size[0]*size[1]
	result = [0]*n
	for i in range (n):
		result[i] = [0] * size[0]
	result[0] = matrix2
	i=0
	while i < (size[0]-1):
		i += 1
		result[i] = np.dot(matrix1,matrix2)
		matrix1 = np.linalg.matrix_power(matrix1, i+1)
	result1 = [0] * size[0]
	for i in range(size[0]):
		result1[i] = []
	for i in range(size[0]):
		for j in range (size[0]):
			result1[i] = np. concatenate( [result1[i], result[j][i]])
	return result1


def checkControllability(matrix1,matrix2):
	rangMatrix = np.linalg.matrix_rank(controllabilityMatrix(matrix1,matrix2))
	size = np.shape(matrix2)
	n =size[0]
	if n == rangMatrix:
		return "The matrix is controllable."
	else:
		return "The matrix is not controllable."



import numpy as np
import time
A = np.array([[7,2,3],[0,5,6],[7,8,9]])
B =np.array([[1],[2],[3]])
C = np.array([[1,7,3]])
startTime = time.time()
print("The rank of the matrix A is:")
rank = np.linalg.matrix_rank(A)
print(rank) 
print(checkObservability(A,C)) 
print(checkControllability(A,B))
endTime = time.time()
time = endTime - startTime
print("Time")
print(time)



