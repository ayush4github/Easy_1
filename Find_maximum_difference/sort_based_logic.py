def max_difference(arr):
    arr.sort()
    max_diff = arr[-1]-arr[0]
    return max_diff
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(max_difference(arr))