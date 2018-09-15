# Начало функции
def heapSort(a):
    # У корня дерева инедекс i
    # n - размер дерева
    # Начало функции
    def heap(arr, n, i):
        largest = i
        # Левая часть дерева
        left = 2*i + 1
        # Правая часть дерева
        right = 2*i + 2        
        
        # Смотрим, не больше ли левый ребенок, чем корень
        if left < n and arr[i] < arr[left]:
            largest = left
        # Смотрим, не больше ли правый ребенок, чем корень
        if right < n and arr[largest] < arr[right]:
            largest = right
        # Изменяем корень, если нужно
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i] 
            heap(arr, n, largest)

    n = len(a)
    # Строим дерево
    for i in range(n, -1, -1):
        heap(a, n, i)
    # Последовательно сортируем массив
    for i in range(n-1, 0, -1):
        c=a[i]
        s=a[0]
        a[i]=s
        a[0]=c
        heap(a, i, 0)
    # Возвращаем массив 
    return a
 

# Начало функции
def dwarfSort(arr):
    i = 1
    # Идем в цикле по всем элементам от i до конца массива
    while i < len(arr):
        # Алгоритм находит первое место, где два соседних элемента стоят в неправильном порядке и меняет их местами
        if (arr[i - 1] <= arr[i]):
            i += 1
        else:
            tmp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = tmp
            i-= 1
            if (i == 0):
                i = 1
    # Возвращаем массив            
    return arr


# Начало функции 
def bubbleSort(arr):
    # Переменная n здесь служит для того, чтобы прервать проходы по списку, как только ее значение приблизится к размеру длины строки
    n = 1
    # Цикл for благодаря n сокращается при каждом последующем проходе по while
    while n < len(arr):
        for i in range(len(arr)-n):
              # Сравниваем элементы массива
              if arr[i] > arr[i+1]:
                   arr[i],arr[i+1] = arr[i+1],arr[i]
        n += 1
    # Возвращаем массив 
    return arr


# Начало функции 
def blockSort(arr):
    # Мфксимальный элемент
    largest = int(max(arr))
    # Количество элементов в массива
    length = int(len(arr))
    # Размер блока
    size = int(largest//length)
    # Заполняем массив блока
    block = [[] for t in range(length)]
    # Проходим в цикле по i по всему массиву
    for i in range(length):
        j = int(arr[i]//size)
        if j < length:
            # Добавляем эллемент в массив
            block[j].append(arr[i])
        else:
            # Добавляем эллемент в массив
            block[length - 1].append(arr[i])
    # Осуществляем пузырьковую сортировку
    for i in range(length):
        bubbleSort(block[i])
    # Создаем результурующий массив 
    result = []
    for i in range(length):
        result = result + block[i]
    
    # Возвращаем массив  
    return result 
