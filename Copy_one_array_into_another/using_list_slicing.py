def copy_array(arr):
    copied_array = arr[:]
    return copied_array
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(copy_array(arr))