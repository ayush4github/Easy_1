def find_second_smallest(arr):
    smallest = float('inf')
    second_smallest = float('inf')
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_second_smallest(arr))