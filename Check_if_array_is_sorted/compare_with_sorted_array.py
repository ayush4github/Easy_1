def is_sorted(arr):
    return arr == sorted(arr)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(is_sorted(arr))