def find_second_largest(arr):
    largest = max(arr)
    second_largest = float('-inf')
    for num in arr:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_second_largest(arr))