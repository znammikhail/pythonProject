def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        x = arr[len(arr)-1]
        arr.pop()
        return x + sum(arr)

print(sum([1,2,3,4,5]))
