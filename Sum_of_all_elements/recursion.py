def find_sum(arr, index = 0):
    if index == len(arr):
        return 0
    return arr[index] + find_sum(arr, index +1)
arr = list(map(int, input("Ënter elements of array separated by space: ").split()))
print(find_sum(arr))