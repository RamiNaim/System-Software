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
 

def heapSort(arr):
    n = len(arr)
 
    for i in range(n, -1, -1):
        heap(arr, n, i)
    for i in range(n-1, 0, -1):
        c=arr[i]
        s=arr[0]
        arr[i]=s
        arr[0]=c
        heap(arr, i, 0)
 
q = int(input())
arr = [int(input()) for i in range(q)]
heapSort(arr)
n = len(arr)
print(arr)
