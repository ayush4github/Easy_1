def copy_array(arr1):
    copied_array = []
    for i in range(len(arr1)):
        copied_array.append(arr1[i])
    return copied_array
arr1 = list(map(int, input("Enter elements of array separated by space: ").split()))
print(copy_array(arr1))