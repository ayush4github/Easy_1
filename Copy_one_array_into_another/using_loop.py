def copy_array(arr):
    copied_array = []
    for num in arr:
        copied_array.append(num)
    return copied_array
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(copy_array(arr))