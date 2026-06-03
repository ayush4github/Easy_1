def helper(arr, index, largest, second):
    if index == len(arr):
        return second
    num = arr[index]
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
    return helper(arr, index +1 , largest, second)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(helper(arr, 0, float('-inf'), float('-inf')))