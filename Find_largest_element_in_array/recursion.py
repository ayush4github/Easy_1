def find_largest(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], find_largest(arr, n-1))
n = int(input("Enter number of elements of array n: "))
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_largest(arr, 5))