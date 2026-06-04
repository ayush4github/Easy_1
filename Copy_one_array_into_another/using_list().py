def copy_array(arr1):
    arr2 = list(arr1)
    return arr2
arr1 = list(map(int, input("Enter elements of array separated by space: ").split()))
print(copy_array(arr1))