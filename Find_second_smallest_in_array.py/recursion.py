def helper(arr, index, smallest, second):
    if index == len(arr):
        return second
    num = arr[index]
    if num < smallest:
        second = smallest
        smallest = num
    elif num < second and num != smallest:
        second = num
    return helper(arr, index+1, smallest, second)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(helper(arr, 0, float('inf'), float('inf')))