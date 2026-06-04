def find_sum(arr):
    total = 0
    for num in arr:
        total+=num
    return total
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_sum(arr))