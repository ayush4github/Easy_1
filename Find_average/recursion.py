def find_average(arr, index = 0):
    if index == len(arr):
        return 0
    total = arr[index] + find_average(arr, index+1)
    if index == 0:
        return total / len(arr)
    return total
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_average(arr))