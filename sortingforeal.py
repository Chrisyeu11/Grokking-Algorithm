def findSmallest(arr):
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # Finds the smallest element in the array
        newArr.append(arr.pop(smallest))  # Adds it to the new array
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
