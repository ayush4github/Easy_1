def search_array(arr, target):
    return arr.index(target)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
target = int(input("Enter target element: "))
print(search_array(arr, target))