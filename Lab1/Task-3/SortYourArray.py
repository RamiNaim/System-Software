from SortAlgos import *

array = input("Введите массив (каждое число через пробел): ")
array = array.split(" ")
for i in range( len(array) ):
    array[i] = float( array[i] )

print("Выберете алгоритм сортировки:")
print("1.Кучей 2.Гномья 3.Пузырьковая 4.Блочная")
sort = int( input() )

if sort == 1:
	array = heapSort(array)
elif sort == 2:
	array = dwarfSort(array)
elif sort == 3:
	array = bubbleSort(array)
elif sort == 4:
	array = blockSort(array)

print("Отсортированный массив: ")
print( array )
