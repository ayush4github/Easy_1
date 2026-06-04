def copy_array(arr, index =0):
    if index == len(arr):
        return []
    return arr[index] + copy_array(arr, index+1)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(copy_array(arr))