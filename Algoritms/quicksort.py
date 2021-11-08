def quicksort(arr):
    '''быстрая сортировка'''
    if len(arr) < 2:
        return arr
    else:
        sr = arr[0]
        left = [i for i in arr[1:] if i <= sr]
        right = [i for i in arr[1:] if i > sr]
        return quicksort(left) + [sr] + quicksort(right)

print(quicksort([1,87,4,5,3,1,8,7,4,3,8,1,5,4,8]))

