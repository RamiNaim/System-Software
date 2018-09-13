q = int(input())
arr = [int(input()) for i in range(q)]

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
        if j != length:
            block[j].append(arr[i])
        else:
            block[length - 1].append(arr[i])
 
    for i in range(length):
        bubbleSort(block[i])
 
    result = []
    for i in range(length):
        result = result + block[i]
 
    return result 

print(blockSort(arr))
