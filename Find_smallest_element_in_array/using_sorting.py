def find_smallest(arr):
    arr.sort()
    return arr[0]
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_smallest(arr))