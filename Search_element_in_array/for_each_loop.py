def search(arr, target):
    index = 0
    for num in arr:
        if num == target:
            return index
        index +=1
    return -1
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
target = int(input("Enter target element: "))
print(search(arr, target))