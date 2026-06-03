def find_largest(arr):
    arr.sort()
    return arr[-1]
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_largest(arr))