def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
target = int(input("Enter target element: "))
print(linear_search(arr, target))