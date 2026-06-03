def find_second_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_second_largest(arr))