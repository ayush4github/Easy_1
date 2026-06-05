def search(arr, target):
    if target in arr:
        return "Found"
    else:
        return "Not Found"
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
target = int(input("Enter target element: "))
print(search(arr, target))