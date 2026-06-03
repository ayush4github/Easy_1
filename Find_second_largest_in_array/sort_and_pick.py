def find_second_largest(arr):
    arr.sort()
    return arr[-2]
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_second_largest(arr))