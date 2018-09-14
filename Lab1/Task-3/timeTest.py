from SortAlgos import *
import time, random
from copy import deepcopy as dp

random.seed( time.time() )

data = open("data.txt", "w")
heapTime = dwarfTime = bubbleTime = blockTime = 0

for k in range(100):
	array = random.sample( range(1, 1000), 100 )

	time1 = time.time()
	heapSort( dp(array) )
	d1 = time.time() - time1
	heapTime += d1

	time1 = time.time()
	dwarfSort( dp(array) )
	d2 = time.time() - time1
	dwarfTime += d2

	time1 = time.time()
	bubbleSort( dp(array) )
	d3 = time.time() - time1
	bubbleTime += d3

	time1 = time.time()
	blockSort( dp(array) )
	d4 = time.time() - time1
	blockTime += d4

	data.write( str(k) + " " + str(d1 * 1000 * 1000) + " " + str(d2 * 1000 * 1000) + " " + str(d3 * 1000 * 1000) + " " + str(d4 * 1000 * 1000) + "\n"  )

print( "Среднее время сортировки массива из 100 элементов (в нс)" )
print( "Кучей:       " + str(heapTime * 1000 * 1000 / 100) )
print( "Гномья:      " + str(dwarfTime * 1000 * 1000 / 100) )
print( "Пузырьковая: " + str(bubbleTime * 1000 * 1000 / 100) )
print( "Блочная:     " + str(blockTime * 1000 * 1000 / 100) )

data.close()