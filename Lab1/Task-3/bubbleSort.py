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
            
bubbleSort(arr)
print(arr)
