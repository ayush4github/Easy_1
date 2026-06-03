def find_second_smallest(arr):
    smallest = min(arr)
    second_smallest = float("inf")
    for num in arr:
        if num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_second_smallest(arr))