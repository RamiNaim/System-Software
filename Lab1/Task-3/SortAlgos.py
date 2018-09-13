def heapSort(a):

    def heap(arr, n, i):
        largest = i 
        left = 2*i + 1     
        right = 2*i + 2        
 
        if left < n and arr[i] < arr[left]:
            largest = left
   
        if right < n and arr[largest] < arr[right]:
            largest = right
  
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i] 
            heap(arr, n, largest)

    n = len(a)
 
    for i in range(n, -1, -1):
        heap(a, n, i)
    for i in range(n-1, 0, -1):
        c=a[i]
        s=a[0]
        a[i]=s
        a[0]=c
        heap(a, i, 0)

    return a
 

def dwarfSort(arr):
    i = 1
    while i < len(arr):
        if (arr[i - 1] <= arr[i]):
            i += 1
        else:
            tmp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = tmp
            i-= 1
            if (i == 0):
                i = 1
    return arr


def bubbleSort(arr):
    n = 1 
    while n < len(arr):
        for i in range(len(arr)-n):
              if arr[i] > arr[i+1]:
                   arr[i],arr[i+1] = arr[i+1],arr[i]
        n += 1            
    return arr


def blockSort(arr):
    largest = int(max(arr))
    length = int(len(arr))
    size = int(largest//length)
 
    block = [[] for t in range(length)]
    for i in range(length):
        j = int(arr[i]//size)
        if j < length:
            block[j].append(arr[i])
        else:
            block[length - 1].append(arr[i])
 
    for i in range(length):
        bubbleSort(block[i])
 
    result = []
    for i in range(length):
        result = result + block[i]
 
    return result 