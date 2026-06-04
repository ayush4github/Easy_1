def copy_array(arr1):
    result = [num for num in arr1]
    return result
arr1 = list(map(int, input("Enter elements of array separated by space: ").split()))
print(copy_array(arr1))