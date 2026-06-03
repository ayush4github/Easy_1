def find_smallest(arr, n):
    if n ==1:
        return arr[0]
    return min(arr[n-1], find_smallest(arr, n-1))
n = int(input("Enter number of elements in array n: "))
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_smallest(arr, n))