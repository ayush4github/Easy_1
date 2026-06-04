def reverse_array(arr):
    return arr[::-1]
arr = list(map(int, input("Enter elements of array separted by space: ").split()))
print(reverse_array(arr))