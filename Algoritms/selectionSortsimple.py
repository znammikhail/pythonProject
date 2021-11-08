import  time
start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))

def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_Sort(arr):
    newArr = []
    for i in range(1,len(arr)):
        smallest = find_Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arr = [2,7,64,2,3,6,54,2,7,5,2,40,7,5,6,24,0,7]

print(selection_Sort(arr))


