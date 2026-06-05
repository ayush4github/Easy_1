def search_array(arr, target, index=0):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return search_array(arr, target, index+1)
arr = list(map(int, input("Enter element of array separated by space: ").split()))
target = int(input("Enter target element: "))
print(search_array(arr, target))