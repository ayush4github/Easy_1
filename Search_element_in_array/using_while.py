def search_array(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i +=1
    return -1
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
target = int(input("Enter target element: "))
print(search_array(arr, target))