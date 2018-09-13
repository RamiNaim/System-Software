from SortAlgos import *
import time, random
from copy import deepcopy as dp

random.seed( time.time() )

data = open("data.txt", "w")

for k in range(100):
	array = random.sample( range(1, 101), 10 )

	time1 = time.time()
	heapSort( dp(array) )
	heapTime = time.time() - time1

	time1 = time.time()
	dwarfSort( dp(array) )
	dwarfTime = time.time() - time1

	time1 = time.time()
	bubbleSort( dp(array) )
	bubbleTime = time.time() - time1

	time1 = time.time()
	blockSort( dp(array) )
	blockTime = time.time() - time1

	data.write( str(k) + " " + str(heapTime * 1000 * 1000) + " " + str(dwarfTime * 1000 * 1000) + " " + str(bubbleTime * 1000 * 1000) + " " + str(blockTime * 1000 * 1000) + "\n"  )

print( "Среднее время сортировки массива из 10 элементов (в нс)" )
print( "Кучей:       " + str(heapTime * 1000 * 1000) )
print( "Гномья:      " + str(dwarfTime * 1000 * 1000) )
print( "Пузырьковая: " + str(bubbleTime * 1000 * 1000) )
print( "Блочная:     " + str(blockTime * 1000 * 1000) )

data.close()