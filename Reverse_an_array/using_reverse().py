def reverse_array(arr):
    arr.reverse()
    return arr
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(reverse_array(arr))