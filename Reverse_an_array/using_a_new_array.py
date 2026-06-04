def reverse_array(arr):
    result = []
    for i in range(len(arr)-1, -1, -1):
        result.append(arr[i])
    return result
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(reverse_array(arr))