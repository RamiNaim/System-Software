q = int(input())
arr = [int(input()) for i in range(q)]

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
            
dwarfSort(arr)
print(arr)
