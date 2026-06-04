def reverse_array(arr):
    n= len(arr)
    for i in range(n//2):
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return arr
arr = list(map(int, input("Ënter the elements of array separated by space: ").split()))
print(reverse_array(arr))