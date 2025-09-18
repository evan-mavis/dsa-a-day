def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = temp
        
    return arr
        
    
print(insertion_sort([4,2,6,5,1,3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """