import random


#Завтра как вчера
def alg1(data):
	list_sg = []
	list_sg.append( data[0] )
	for i in range(1,50):
		list_sg.append( data[i-1] )
	return list_sg

#Скользящее среднее
def alg2(data):
	list_sg = []
	n = 3
	list_sg.append( data[0] )
	list_sg.append( (data[0]+data[1])/2.0 )
	summ = data[0]+data[1]
	for i in range(2,50):
		summ += data[i]
		list_sg.append( 1.0 * summ / n )
		summ -= data[i-2]
	return list_sg

#Взвешенное среднее
def alg3(data):
	list_sg = []
	weights = [ i/50. for i in range(1, 51)]
	sum_weight = 0
	sum_weighted = 0
	for i in range(50):
		sum_weight += weights[i]
		sum_weighted += data[i] * weights[i]
		y = 1.0 * sum_weighted / sum_weight
		list_sg.append( y )
	return list_sg


def alg3_v2(data):
	weights = [0.05, 0.1, 0.15, 0.3, 0.4]
	list_sg = [data[0]]
	for i in range(1, 50):
		y = 0
		for j in range( len(weights) ):
			if (i - ( len(weights) - j) ) < 0:
				continue
			y += data[ i - (len(weights) - j) ] * weights[j]
		list_sg.append( y )
	return list_sg



# Простое экспоненциальное сглаживание
def alg4(data):
	list_sg = []
	alpha = 0.3
	list_sg.append( data[0] )
	for i in range(1,50):
		list_sg.append( alpha*data[i]+(1-alpha)*list_sg[i-1] )
	return list_sg


data = []
for i in range(50):
	data.append( random.randint(0, 40) )

alg1_res = alg1(data)
alg2_res = alg2(data)
alg3_res = alg3_v2(data)
alg4_res = alg4(data)

d = open("Data.txt", "w")
a1 = open("Alg1.txt", "w")
a2 = open("Alg2.txt", "w")
a3 = open("Alg3.txt", "w")
a4 = open("Alg4.txt", "w")

for i in range(50):
	d.write( str(data[i]) + " " + str(i) + "\n" )
	a1.write( str(alg1_res[i]) + " " + str(i) + "\n" )
	a2.write( str(alg2_res[i]) + " " + str(i) + "\n" )
	a3.write( str(alg3_res[i]) + " " + str(i) + "\n" )
	a4.write( str(alg4_res[i]) + " " + str(i) + "\n" )

a1.close()
a2.close()
a3.close()
a4.close()



