def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_smallest(arr))